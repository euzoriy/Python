# -*- coding: utf-8 -*-
"""
Created on Fri May 24 11:24:18 2019

@author: ievgenz
"""
import sqlite3
import pandas as pd

conn = sqlite3.connect('files.db')
c = conn.cursor()

tableName = "t_files"
stmt = "SELECT count(name) FROM sqlite_master WHERE type='table' AND name='"+tableName+"' "

c.execute(stmt)
if c.fetchone()[0]==1:{
        print("there is a table named '{}'".format(tableName))
        }

tmp = c.execute('SELECT rowid, file_path FROM '+tableName)

count = 0

t_table="T_Temp"

for row in tmp:
    print(row)
    dfs = pd.read_excel(row[1], sheetname=None)
    
    for table, df in dfs.items():
        #df.to_sql(t_table, conn)
        print ("Pfle: '{}' tab: '{}' imported".format(row[1], table))
        #TODO copy data to special table and clean Temp table after
        
    
    
    
    count+=1
#    if count >5:
#        break
        
##Clean up data 
#tmp = c.execute('delete FROM '+tableName)
#conn.commit()

print ("Done!")