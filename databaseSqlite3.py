#!/usr/bin/python3.6
import sqlite3
import time
conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datastamp TEXT, keyword TEXT, value REAL)')

def insert_table():
    unix_value=int(input("Enter unix time stamp: "))
    date_value=str(input("Enter date e.g 2018-01-02: "))
    Keyword_value=str(input("Enter keyword: "))
    number_value=int(input("Enter the number: "))
    c.execute('INSERT INTO stuffToPlot VALUES(?,?,?,?)',(unix_value, date_value, Keyword_value, number_value))
    conn.commit()
    c.close()
    conn.close()

#create_table()
#insert_table()

def delete_table():
   conn = sqlite3.connect('tutorial.db')
   c = conn.cursor()
   number_value=input("Delete on the basis of number: ")
   print("We are going to delete...")
   time.sleep(1)
   c.execute('DELETE FROM stuffToPlot WHERE value = (?)', (number_value))
   conn.commit()
   c.close()
   conn.close()
   print("...Deleted!!...")
def select_table():
    conn = sqlite3.connect('tutorial.db')
    c = conn.cursor()
    for row in c.execute('SELECT * FROM stuffToPlot'):
        print(row)
    conn.commit()
    c.close()
    conn.close()

value=input("Press 'v' to view rows\nPress 'd' to delete rows\nPress 'i' to insert rows\n")
#print(value)
if value in 'd':
   print("calling Delete function delete_table")
   delete_table()
elif value in 'v':
   print("calling Select function select_table")
   select_table()
elif value in 'i':
   print("calling insert function insert_table")
   insert_table()
else:
   print("Fuck off WTH")     
