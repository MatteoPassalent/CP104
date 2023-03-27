"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Your Name
ID:      Your ID
Email:   your email@mylaurier.ca
__updated__ = "2022-11-09"
-------------------------------------------------------
"""
# Imports

# Constants


user_values = [1, 5, 8, 4]

max_value = user_values[0]
for i in range(len(user_values)):
    if user_values[i] >= max_value:
        max_value = user_values[i]
        print(max_value)
