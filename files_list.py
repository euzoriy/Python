# -*- coding: utf-8 -*-
"""
Created on Thu May 23 16:03:02 2019

@author: ievgenz
"""

import os
import os.path
import re

ptrn = re.compile('(([^~])\d){4}(([-])(\d){0,3}){0,2}(.xls(x){0,1})')

for dirpath, dirnames, filenames in os.walk("L:\Data_Setups"):
    #for filename in [f for f in filenames if (f.endswith(".xlsx") or f.endswith(".xls"))]:
    for filename in [f for f in filenames if ptrn.match(f)]:
        print (os.path.join(dirpath, filename))