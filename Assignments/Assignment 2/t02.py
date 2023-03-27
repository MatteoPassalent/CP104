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

while True:
    try:
        num = int(input('Enter a positive digit number: '))
        if num < 10 or num > 99:
            raise ValueError
        break
    except ValueError:
        print("Invalid integer. The number must be two digits.")

base = 10

floor = num // base
modulus = num % base

answer = floor * modulus
print()
print(f'The product of the digits of {num} is {answer}')
