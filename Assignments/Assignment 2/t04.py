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

cake = int(input('Number of pieces of cake: '))
people = int(input('Number of party-goers: '))

received = cake // people
leftover = cake % people

print()
print(f'Each party-goer receives {received} pieces of cake')
print(f'Pieces of cake that won’t be distributed: {leftover}')
