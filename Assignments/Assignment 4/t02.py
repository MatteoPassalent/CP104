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

from functions import pollution_level

aqi = int(input("Enter AQI: "))

level = pollution_level(aqi)

print(level)
