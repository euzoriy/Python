# -*- coding: utf-8 -*-
"""
Created on Thu May 23 15:26:14 2019

@author: ievgenz
"""

# -*- coding: utf-8 -*-
"""
Created on Thu May 23 15:05:23 2019

@author: ievgenz
"""
import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()


# Create table if not exists
c.execute('''CREATE TABLE if not exists t_files
             (date text, trans text, symbol text, qty real, price real)''')

c.execute('''CREATE TABLE IF NOT EXISTS projects (
        id integer PRIMARY KEY,
        name text NOT NULL,
        begin_date text,
        end_date text
        );''')

c.execute('''CREATE TABLE IF NOT EXISTS tasks ( 
        id integer PRIMARY KEY, 
        name text NOT NULL, 
        priority integer, 
        project_id integer NOT NULL, 
        status_id integer NOT NULL, 
        begin_date text NOT NULL, 
        end_date text NOT NULL, 
        FOREIGN KEY (project_id) REFERENCES projects (id)
        );''')

# Never do this -- insecure!
symbol = 'RHAT'
c.execute("SELECT * FROM t_files WHERE symbol = '%s'" % symbol)

# Do this instead
t = ('RHAT',)
c.execute('SELECT * FROM t_files WHERE symbol=?', t)
print(c.fetchone())

# Larger example that inserts many records at a time
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]

c.executemany('INSERT INTO t_files VALUES (?,?,?,?,?)', purchases)
for row in c.execute('SELECT * FROM t_files ORDER BY price'):
            print(row)
            