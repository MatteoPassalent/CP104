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
from functions import multiply_fractions

numerator1 = int(input('Numerator 1: '))
denominator1 = int(input('Denominator 1: '))
numerator2 = int(input('Numerator 2: '))
denominator2 = int(input('Denominator 2: '))

answer = multiply_fractions(numerator1, denominator1, numerator2, denominator2)

print()
print(f'Result: {answer[0]}/{answer[1]} = {answer[2]:0.3f}')
