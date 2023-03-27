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

length = float(input('Foundation length (m): '))
width = float(input('Foundation width (m): '))
f_height = float(input('Foundation height (m): '))
w_height = float(input('Wall height (m): '))
cost_concrete = float(input('Cost of concrete ($/m^3): '))
cost_bricks = float(input('Cost of bricks ($/m^2): '))

concrete = length * width * f_height
cost_fondation = concrete * cost_concrete
bricks = (length * w_height * 2) + (width * w_height * 2)
cost_wall = bricks * cost_bricks
total_cost = cost_wall + cost_fondation

print()
print(f'Concrete needed for foundation (m^3): {concrete:.2f}')
print(f'Cost of concrete: ${cost_fondation:,.2f}')
print(f'Bricks needed for walls (m^2): {bricks:.2f}')
print(f'Cost of bricks: ${cost_wall:,.2f}')
print(f'Total cost: ${total_cost:,.2f}')
