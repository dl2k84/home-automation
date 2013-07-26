import array
import sqlite3
import sys
import io
import time
import reference


def getLightingStatus():
  conn = sqlite3.connect('sqlite3/homeautomation.db')
  with conn:    
  
    cur = conn.cursor()
    # Get current lighting status
    cur.execute("SELECT Mode FROM STATUS_LIGHTING")

    return cur.fetchone()[0]


def getTotalModes():
  conn = sqlite3.connect('sqlite3/homeautomation.db')
  with conn:    
    
    cur = conn.cursor()

    # Get total possible modes
    cur.execute("SELECT COUNT(*) FROM REFERENCE_LIGHTING")

    return cur.fetchone()[0]


def setLighting(stateId):
  conn = sqlite3.connect('sqlite3/homeautomation.db')
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
      code = reference.getReferenceCode("REFERENCE_LIGHTING_CODES", stateId)
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
  conn = sqlite3.connect('sqlite3/homeautomation.db')
  with conn:    
    
    cur = conn.cursor()

    cur.execute("\
      UPDATE STATUS_LIGHTING\
      SET Mode = :mode"
      , { "mode": stateId })
