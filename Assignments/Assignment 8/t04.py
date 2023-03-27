"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matteo Passalent
ID:      210597410
Email:   pass7410@mylaurier.ca
__updated__ = "2022-11-27"
-------------------------------------------------------
"""

from functions import is_valid_isbn

isbn = input("Enter ISBN: ")

valid = is_valid_isbn(isbn)

print(valid)
