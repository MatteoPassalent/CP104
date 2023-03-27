"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matteo Passalent
ID:      210597410
Email:   pass7410@mylaurier.ca
__updated__ = "2022-10-19"
-------------------------------------------------------
"""
from functions import date_extract

date_input = int(input('Enter a date in the format MMDDYYYY: '))

reformatted_date = date_extract(date_input)

print()
print(
    f'The reformatted date: {reformatted_date[0]}/{reformatted_date[1]}/{reformatted_date[2]}')
