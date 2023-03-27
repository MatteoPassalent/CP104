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


def factorial(num):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of num.
    Use: product = factorial(num)
    -------------------------------------------------------
    Parameters:
        num - number to factorial (int > 0)
    Returns:
        product - num! (int)
    ------------------------------------------------------
    """
    total = 1

    for digit in range(1, num + 1):
        total = total * digit

    return total


def calories_burned(per_minute, minutes):
    """
    -------------------------------------------------------
    Prints a table of the number of calories burned every
    five minutes given the number of calories burned per minute
    an the total number of minutes run.
    Use: calories_burned(per_minute, minutes)
    -------------------------------------------------------
    Parameters:
        per_minute - calories burned per minute (float)
        minutes - total number of minutes ran (int)
    Returns:
        None
    ------------------------------------------------------
    """

    for num in range(5, minutes + 1, 5):
        calories = num * per_minute
        print(f'{num:3d}:{calories:6.1f}')

    return


def open_triangle(num_rows):
    """
    ------------------------------------------------------
    Takes integer parameter and prints a triangle of # characters with empty center
    Use: open_triangle(num_rows)
    ------------------------------------------------------
    Parameters:
        num_rows - number of rows in triangle
    Returns:
        None
    ------------------------------------------------------
    """

    for i in range(2, num_rows + 2):

        print(("#" + (" " * (i - 2) + "#")))

    return


def multiplication_table(start, stop):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start to stop.
    Use: multiplication_table(start, stop)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        stop - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """
    print("       ", end="")
    for num in range(start, stop + 1):

        print(f"{num:5d}", end="")

    print()
    dashes = "-----" * (stop - start + 1)
    print(f"       {dashes}")

    for num1 in range(start, stop + 1):
        print(f"{num1:5d} |", end="")

        for num2 in range(start, stop + 1):
            product = num1 * num2
            print(f'{product:5d}', end="")

        print()

    return


def range_total(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum count values from start by increment.
    Use: total = range_total(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """
    num = 0
    for i in range(start, start + (count * increment), increment):
        num = num + i

    return(num)
