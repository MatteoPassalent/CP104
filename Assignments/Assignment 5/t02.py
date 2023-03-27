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
from functions import calories_burned

per_minute = float(input("Enter calories burnt per minute: "))
minutes = int(input("Enter time working out: "))

product = calories_burned(per_minute, minutes)
