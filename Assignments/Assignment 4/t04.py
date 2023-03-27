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

from functions import rgb_mix

rgb1 = input("Enter (red/blue/green) colour: ")
rgb2 = input("Enter (red/blue/green) colour: ")

colour = rgb_mix(rgb1, rgb2)

print(colour)
