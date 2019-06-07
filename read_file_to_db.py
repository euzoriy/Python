# -*- coding: utf-8 -*-
"""
Created on Thu May 23 16:03:02 2019

@author: ievgenz
"""

import os
import os.path
import re
import sqlite3

conn = sqlite3.connect('files.db')
c = conn.cursor()

# Create table if not exists
tableName = "t_files"
stmt = "SELECT count(name) FROM sqlite_master WHERE type='table' AND name='"+tableName+"' "

c.execute(stmt)
if c.fetchone()[0]==1:{
        print("there is a table named ",tableName)
        }

c.execute('''CREATE TABLE IF NOT EXISTS '''+tableName+''' (
        file_name text NOT NULL,
        file_path text NOT NULL UNIQUE,        
        date_modified real,
        date_last_read real
        );''')

tmp = []

ptrn = re.compile('(\d){4}(([-])(\d){0,3}){0,2}(.xls(x){0,1})')
#ptrn = re.compile('(([^~])\d){4}(([-])(\d){0,3}){0,2}(.xls(x){0,1})')
#ptrn = re.compile('(([^~])\d){4}([-])(.)(.xls(x){0,1})')
#ptrn = re.compile('(\b(\d){4}(.)*(xls(x){0,1})\b)')


#for dirpath, dirnames, filenames in os.walk("L:\Data_Setups"):
#    for filename in [f for f in filenames if ptrn.match(f)]:
#        print (os.path.join(dirpath, filename))
#        fpath =os.path.join(dirpath, filename)
#        print ("{},{},{}".format(filename,fpath,os.path.getctime(fpath)))
#        tmp.append((filename,fpath,os.path.getctime(fpath),None))
counting = 0
good_fn = 0
    
for dirpath, dirnames, filenames in os.walk("L:\Data_Setups"):
#    for filename in [f for f in filenames if (f.endswith(".xlsx") or f.endswith(".xls"))]:
#    for dirnames in [d for d in dirpath if ('old' not in d and 'obs' not in d)]:
    if 'old' in dirpath.lower() or 'obs' in dirpath.lower():
#        print ('Excluding ' + dirpath)
        counting+=1
    else:
        for filename in [f for f in filenames if ptrn.match(f)]:
    #    and ((f.endswith(".xlsx") or f.endswith(".xls")) and '~' not in f )]:
            fpath =os.path.join(dirpath, filename)
            print ("{},{},{}".format(filename,fpath,os.path.getctime(fpath)))
            tmp.append((filename,fpath,os.path.getctime(fpath),None))
            good_fn +=1
    
    
#tmp = [('6527.xlsx','L:\Data_Setups\6527\docs\6527.xlsx',1,2),
#       ('6528.xlsx','L:\Data_Setups\6528\docs\6528.xlsx',1,2),
#       ('6529.xlsx','L:\Data_Setups\6529\docs\6529.xlsx',1,2),
#       ('6530.xlsx','L:\Data_Setups\6530\docs\6530.xlsx',1,2),
#       ('6532.xlsx','L:\Data_Setups\6532\docs\6532.xlsx',1,2)]
    

c.executemany("INSERT INTO "+tableName+" VALUES (?,?,?,?)", tmp)
conn.commit()

print ("Found {} good files, omited {} folders".format(good_fn,counting))
print ("Done!")