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
from functions import mow_lawn

width = float(input('Width (m): '))
length = float(input('Length (m): '))
speed = float(input('Speed (m^2/minute): '))

time = mow_lawn(width, length, speed)

print()
print(f'Mowing the lawn takes {time:.0f} minutes')
