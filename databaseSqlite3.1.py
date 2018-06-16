#!/usr/bin/python3.6
import sqlite3
import time
import database
import random
conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datastamp TEXT, keyword TEXT, value REAL)')

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Java'
    value = random.randrange(0,10)
    c.execute('INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?,?,?,?)',
              (unix, date, keyword, value))
    conn.commit()



