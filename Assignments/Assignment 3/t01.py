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

from functions import feet_to_acres

feet = float(input("Square footage: "))

acres = feet_to_acres(feet)

print()
print(f'{acres:,.2f} acres is equivalent to {feet:,.2f} square feet')
