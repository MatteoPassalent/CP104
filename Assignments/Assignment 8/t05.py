"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matteo Passalent
ID:      210597410
Email:   pass7410@mylaurier.ca
__updated__ = "2022-11-27"
-------------------------------------------------------
"""

from functions import is_word_chain

length = int(input('Enter list length: '))
word_list = []

for i in range(length):
    word = input("Enter word: ")
    word_list.append(word)

word_chain = is_word_chain(word_list)

print(word_chain)
