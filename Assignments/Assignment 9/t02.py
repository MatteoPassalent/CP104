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

from functions import file_integers

fh = open("numbers.txt")
numbers = file_integers(fh)
fh.close()
print(numbers)
