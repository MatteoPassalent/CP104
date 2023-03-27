"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matteo Passalent
ID:      210597410
Email:   pass7410@mylaurier.ca
__updated__ = "2022-12-04"
-------------------------------------------------------
"""

from functions import file_head

linecount = int(input("Linecount: "))

fh = open('t01.py')
file_head(fh, linecount)
fh.close()
