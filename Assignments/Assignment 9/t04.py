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

from functions import number_lines

fh_in = open('wilde.txt', 'r')
fh_out = open('wilde_numbered.txt', 'w')
number_lines(fh_in, fh_out)
fh_out.close()
fh_out = open('wilde_numbered.txt', 'r')

before = fh_in.read()
output = fh_out.read()

fh_in.close()
fh_out.close()

print(output)
