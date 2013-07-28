import sqlite3
import json
import db


# Returns reference data as JSONArray
def getReference(table):
  conn = db.getDbConnection()
  with conn:

    cur = conn.cursor()

    # Get NEC code for lights
    sql = "SELECT * FROM " + table
    cur.execute(sql)

    rows = cur.fetchall()

    map = []
    for r in rows:
      row = { r[0]: r[1] }
      map.append(row)
   
    return json.dumps(map)


# Returns byte code array
def getReferenceCode(table, state, makerName, hasInputMask=False):
  conn = db.getDbConnection()
  with conn:

    cur = conn.cursor()

    # Get NEC code for lights
    sql = "\
      SELECT Code\
      FROM " + table + "\
      WHERE StateId = :state\
      AND MakerName = :maker"
    cur.execute(sql, { "state": state, "maker": makerName })

    code = cur.fetchone()[0]
    if (hasInputMask):
      return code
    else:
      return code.decode("hex")

# Returns byet code and human readable value
def getReferenceCodeAndValue(table, typeName, makerName):
  conn = db.getDbConnection()
  with conn:

    cur = conn.cursor()

    # Get code and human readable value for specified code type and maker
    sql = "\
      SELECT Code, CodeValue\
      FROM " + table + "\
      WHERE TypeName = :type\
      AND MakerName = :maker"
    cur.execute(sql, { "type": typeName, "maker": makerName })
    return cur.fetchone()


# Returns StateId for the given literal aircon mode value
def getAirconModeId(stateValue):
  conn = db.getDbConnection()
  with conn:

    cur = conn.cursor()

    # Get Stateid for specified stateValue
    sql = "SELECT StateId FROM REFERENCE_AIRCON_MODE WHERE Value = :value"
    cur.execute(sql, { "value": stateValue })

    return cur.fetchone()[0]
