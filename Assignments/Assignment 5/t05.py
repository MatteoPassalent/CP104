"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matteo Passalent
ID:      210597410
Email:   pass7410@mylaurier.ca
__updated__ = "2022-11-06"
-------------------------------------------------------
"""
from functions import range_total

start = int(input("Start: "))
increment = int(input("Increment: "))
count = int(input("Count: "))

result = range_total(start, increment, count)

print(result)
