import sqlite3
import json


# Returns reference data as JSONArray
def getReference(table):
  conn = sqlite3.connect('sqlite3/homeautomation.db')
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
def getReferenceCode(table, state):
  conn = sqlite3.connect('sqlite3/homeautomation.db')
  with conn:

    cur = conn.cursor()

    # Get NEC code for lights
    sql = "SELECT Code FROM " + table + " WHERE StateId = :state"
    cur.execute(sql, { "state": state })

    return cur.fetchone()[0].decode("hex")
