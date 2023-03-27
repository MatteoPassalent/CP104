"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matteo Passalent
ID:      210597410
Email:   pass7410@mylaurier.ca
__updated__ = "2022-12-04"
-------------------------------------------------------
"""

from functions import student_info

students = open("students.txt", "r")
l_id, h_id, avg = student_info(students)
students.close()

print(f'{l_id}, {h_id}, {avg:.2f}')
