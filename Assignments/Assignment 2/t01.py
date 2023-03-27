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

sales = int(input('Enter the total sales: $'))

TAX = 18.50

total = sales * (TAX / 100)

print()
print('Projected Tax Report')
print('--------------------------')
print(f'Total sales:   $ {sales:,.2f}')
print(f"Annual tax:    % {TAX:,.2f}")
print('--------------------------')
print(f"Tax:           $  {total:,.2f}")
