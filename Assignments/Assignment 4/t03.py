"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matteo Passalent
ID:      210597410
Email:   pass7410@mylaurier.ca
__updated__ = "2022-10-30"
-------------------------------------------------------
"""

from functions import product_largest

v1 = float(input("Input value 1: "))
v2 = float(input("Input value 2: "))
v3 = float(input("Input value 3: "))

product = product_largest(v1, v2, v3)

print(f'{product:.0f}')
