"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matteo Passalent
ID:      210597410
Email:   pass7410@mylaurier.ca
__updated__ = "2023-01-22"
-------------------------------------------------------
"""

from functions import find_subs

string = 'It was a really, really, big really assignment. really'
sub = 'real'

locations = find_subs(string, sub)

print(locations)
