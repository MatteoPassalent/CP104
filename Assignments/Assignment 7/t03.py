"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matteo Passalent
ID:      210597410
Email:   pass7410@mylaurier.ca
__updated__ = "2022-11-18"
-------------------------------------------------------
"""

from functions import list_indexes

length = int(input("Enter list length: "))
values = []

for i in range(length):
    num = int(input("Enter digit: "))
    values.append(num)

target = int(input("Enter Target: "))

locations = list_indexes(values, target)
print(locations)
