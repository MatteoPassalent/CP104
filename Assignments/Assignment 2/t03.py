"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matteo Passalent
ID:      210597410
Email:   pass7410@mylaurier.ca
__updated__ = "2022-10-09"
-------------------------------------------------------
"""

date = int(input('Enter a date in the format DDMMYYYY: '))

day = date // 1000000
month = int((date % 1000000) / 10000)
year = date % 10000

print()
print(f'The reformatted date: {year:04d}/{month:02d}/{day:02d}')
