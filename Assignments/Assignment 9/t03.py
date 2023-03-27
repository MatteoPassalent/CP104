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

from functions import file_stats

fh = open('addresses.txt')
ucount, lcount, dcount, wcount = file_stats(fh)
fh.close()

print(ucount, lcount, dcount, wcount)
