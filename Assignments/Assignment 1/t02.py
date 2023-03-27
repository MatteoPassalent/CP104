"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matteo Passalent
ID:      210597410
Email:   pass7410@mylaurier.ca
__updated__ = "2023-01-22"
-------------------------------------------------------
"""

from functions import file_analyze

fv = open('t02file', 'r')

u, l, d, w, r = file_analyze(fv)

print(u, l, d, w, r)
