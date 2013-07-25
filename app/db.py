import sqlite3
import sys

v = 'bright'

con = sqlite3.connect('sqlite3/homeautomation.db')

with con:    
    
    cur = con.cursor()    
    cur.execute("SELECT Id\
        FROM REFERENCE_LIGHTING\
        WHERE Value = :value\
        ", {"value": v})

    row = cur.fetchone()

    print row[0]
