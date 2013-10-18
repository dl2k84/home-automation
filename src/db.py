import array
import sqlite3
import sys
import io
import time
import reference
from flask import json
import subprocess


def getDbConnection():
  return sqlite3.connect('sqlite3/homeautomation.db')


def getLightingStatus():
  conn = getDbConnection()
  with conn:
  
    cur = conn.cursor()
    # Get current lighting status
    cur.execute("SELECT Mode FROM STATUS_LIGHTING")

    return cur.fetchone()[0]


def getTotalModes():
  conn = getDbConnection()
  with conn:
    
    cur = conn.cursor()

    # Get total possible modes
    cur.execute("SELECT COUNT(*) FROM REFERENCE_LIGHTING")

    return cur.fetchone()[0]


def setLighting(stateId):
  conn = getDbConnection()
  with conn:
    
    cur = conn.cursor()

    # Get total possible modes
    totalModes = getTotalModes()

    # Get current lighting status
    currentMode = getLightingStatus()

    if (currentMode != stateId):
      updateLightingStatus(stateId)

      # Only transmit signal if the current and requested modes differ
      s = currentMode

      # Open stream to IrDA device
      # TODO currently hardcoding device as /dev/hidraw3 - needs to be configurable
      # TODO currently hardcoding maker name NEC
      code = reference.getReferenceCode("REFERENCE_LIGHTING_CODES", stateId, "nec")
      o = io.open("/dev/hidraw3", "wb+")

      with o:

        while (s != stateId):
          # Sleep 3s so as to not flood the IrDA device
          time.sleep(3)
          # Send light code to IrDA and flush stream
          o.write(code)
          o.flush()
          if (s == 0):
            # wrap around
            s = totalModes
          s -= 1
        print "Closing IrDA handle"
        o.close()


def updateLightingStatus(stateId):
  conn = getDbConnection()
  with conn:
    
    cur = conn.cursor()

    sql = "UPDATE STATUS_LIGHTING SET Mode = :mode"
    cur.execute(sql, { "mode": stateId })


def getAirconStatus():
  conn = getDbConnection()
  with conn:
  
    cur = conn.cursor()
    # Get current aircon status
    cur.execute("SELECT Code FROM STATUS_AIRCON")

    code = bytearray.fromhex(cur.fetchone()[0])

    # Header contains the following 4 bytes
    # IrDA control code, format code, code1 length, code2 length
    # code1Offset comes after the header
    code1Offset = 3
    code1LengthIndex = 2
    # Value is represented in bits, so divide 8 for byte length
    code1Length = code[2] / 8
    # code 2 offset = 4 (control header) + code 1 length bytes
    code2Offset = code1Offset + code1Length
    # the flags indicating 
    # ac/dehimidifier/heater mode and
    # on/off is the 6th byte in code2
    modeIndex = code2Offset + 6
    modeFlag = code[modeIndex]
    turnOn = isBitFlagSet(modeFlag, 0)

    # TODO Dirty code for the sake of getting things working
    # Currently has intimiate knowledge of mode codes
    # Control code below should be gotten from DB. Move it there later.
    if turnOn:
      mode = "error"
      # 0x21 = Dehumidifier + on
      # 0x31 = Airconditioner
      # 0x41 = Heater + on
      if modeFlag == 0x21:
        mode = "dehumidifier"
      elif modeFlag == 0x31:
        mode = "aircon"
      elif modeFlag == 0x41:
        mode = "heater"
    else:
      mode = "error"
      # 0x20 = Dehumidifier + off
      # 0x30 = Airconditioner
      # 0x40 = Heater + off
      if modeFlag == 0x20:
        mode = "dehumidifier"
      elif modeFlag == 0x30:
        mode = "aircon"
      elif modeFlag == 0x40:
        mode = "heater"

    # TODO hardcoding to get back panasonic aircon, this should be
    # passed in from request
    referenceTable = "REFERENCE_AIRCON_CODE_TYPE"
    temperatureMin1Name = "temperature-min-1"
    temperatureMin2Name = "temperature-min-2"
    maker = "panasonic"
    temperatureMin1 = reference.getReferenceCodeAndValue(referenceTable, temperatureMin1Name, maker)
    temperatureMin2 = reference.getReferenceCodeAndValue(referenceTable, temperatureMin2Name, maker)
    # temperature1 = 7th byte in code2, temperature2 = 19th byte in code 2
    currentTemperature1Offset = code2Offset + 7
    currentTemperature2Offset = code2Offset + 19
    currentTemperature1 = code[currentTemperature1Offset]
    currentTemperature2 = code[currentTemperature2Offset]
    # Calculate difference between current and min temperature
    temperatureDifference1 = currentTemperature1 - bytearray.fromhex(temperatureMin1[0])[0]
    temperatureDifference2 = currentTemperature2 - bytearray.fromhex(temperatureMin2[0])[0]
    # If turn off code, temperature2 code is reduced by 1 while temperature1 stays same
    if turnOn == False:
      temperatureDifference2 += 1

    temperature = -1
    # Check temperatureDifference1 and temperatureDifference2 equals. If it doesn't, we got a problem with the byte code spec...
    if temperatureDifference1 == temperatureDifference2:
      temperature = int(temperatureMin1[1]) + int(temperatureDifference1 / 2)
  return { "mode": mode, "temperature": temperature, "turnOn": turnOn }


def setAircon(request):
  temperature = request["temperature"]
  mode = request["mode"]
  turnOn = request["turnOn"]

  modeId = reference.getAirconModeId(request["mode"])
  # TODO currently hardcoding maker name Panasonic
  code = reference.getReferenceCode("REFERENCE_AIRCON_CODES", modeId, "panasonic", True)
  code = str(code)

  # Internal spec for input mask
  # TODO Should probably document this somewhere else...
  # g: on/off mask
  # hh: temperature control code 1
  # ii: temperature control code 2
  # Set on/off
  onOffTypeName = "on"
  if turnOn == False:
    onOffTypeName = "off"
  # TODO Hardcoding maker Panasonic, should be passed in from request
  onOffCode = reference.getReferenceCodeAndValue("REFERENCE_AIRCON_CODE_TYPE", onOffTypeName, "panasonic")[0]
  code = str.replace(code, "g", str(onOffCode))

  # TODO Fail/Do not process if requested temperature is not within
  # the min/max temperature values set in REFERENCE_AIRCON_CODE_TYPE

  # Set temperature code 1
  minTemperature1 = reference.getReferenceCodeAndValue("REFERENCE_AIRCON_CODE_TYPE", "temperature-min-1", "panasonic")
  minTemperature2 = reference.getReferenceCodeAndValue("REFERENCE_AIRCON_CODE_TYPE", "temperature-min-2", "panasonic")

  # multiply resulting difference by 2 as each temperature code increments by 2
  temperatureDifference = (temperature - int(minTemperature1[1])) * 2
  targetTemperature1 = int(minTemperature1[0], 16) + temperatureDifference
  targetTemperature2 = int(minTemperature2[0], 16) + temperatureDifference
  if turnOn == False:
    # -1 on code2 if off
    targetTemperature2 -= 1

  temperature1Code = hex(targetTemperature1)[2:].zfill(2)
  temperature2Code = hex(targetTemperature2)[2:].zfill(2)

  code = str.replace(code, "hh", str(temperature1Code))
  code = str.replace(code, "ii", str(temperature2Code)) 

  # TODO Compare with current aircon status. If match, do not send again.

  # Update status and return in human readable JSON format
  updateAirconStatus(code)

  # Send code to airconditioner via IrDA
  o = io.open("/dev/hidraw3", "wb+")

  print code
  with o:
      # Send light code to IrDA and flush stream
      o.write(code.decode("hex"))
      o.flush()
      print "Closing IrDA handle"
      o.close()
  return getAirconStatus()


def updateAirconStatus(code):
  conn = getDbConnection()
  with conn:
    
    cur = conn.cursor()

    sql = "UPDATE STATUS_AIRCON SET Code = :code"
    cur.execute(sql, { "code": code })


def getPresenceCount():
  count = 0
  devices = getRegisteredDevices()
  for name, id in devices.items():
    if (isPresent(id)):
      count += 1

  return count


def getPresence():
  present = []
  devices = getRegisteredDevices()
  for name, id in devices.items():
    if (isPresent(id)):
      present.append(name)

  return present


def isPresent(id):
  returnCode = subprocess.call("l2ping" + " -c 1 " + id, shell = True)
  if (returnCode == 0):
    return True
  return False


def getRegisteredDevices():
  conn = getDbConnection()
  with conn:

    cur = conn.cursor()

    sql = "SELECT * FROM REGISTERED_DEVICES"
    cur.execute(sql)

    devices = {}
    for row in cur.fetchall():
      devices[row[1]] = row[2]

    return devices

    
 
def isBitFlagSet(byte, index):
    return ((byte & (1<<index))!=0)
