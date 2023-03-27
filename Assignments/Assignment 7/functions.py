"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matteo Passalent
ID:      210597410
Email:   pass7410@mylaurier.ca
__updated__ = "2022-11-18"
-------------------------------------------------------
"""


def list_factors(num):
    """
    -------------------------------------------------------
    creates a list of factors of num
    Use: factors = list_factors(num)
    -------------------------------------------------------
    Parameters:
        num - a positive integer (int > 1)
    Returns:
        list - A list of positive integers (list of int)
    ------------------------------------------------------
    """

    list = []
    div = 1
    for i in range(num-1):
        if num % div == 0:
            list.append(div)
        div += 1
    return list


def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: numbers = list_positives()
    -------------------------------------------------------
    Returns:
        numbers - A list of positive integers (list of int)
    ------------------------------------------------------
    """
    digit = None
    numbers = []
    while digit != 0:
        digit = int(input("Enter a positive number: "))
        if digit > 0:
            numbers.append(digit)

    return numbers


def list_indexes(values, target):
    """
    -------------------------------------------------------
    Finds the indexes of target in values.
    Use: indexes = list_indexes(values, target)
    -------------------------------------------------------
    Parameters:
        values - list of value (list of int)
        target - value to look for in num_list (int)
    Returns:
        locations - list of indexes of target (list of int)
    -------------------------------------------------------
    """
    locations = []

    for i in range(len(values)):

        if values[i] == target:
            locations.append(i)

    return locations


def subtract_lists(minuend, subtrahend):
    """
    -------------------------------------------------------
    Updates the list minuend removing from it the values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are not included in the updated list.
    subtrahend is unchanged
    Use: subtract_lists(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to remove from minuend (list)
    Returns:
        None
    ------------------------------------------------------
    """

    for i in range(len(subtrahend)):

        indexes = list_indexes(minuend, subtrahend[i])

        for j in range(len(indexes) - 1, -1, -1):

            minuend.pop(indexes[j])
    return


def is_sorted(values):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = is_sorted(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list)
    Returns:
        in_order - True if values is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """

    in_order = True
    index = -1

    for i in range(len(values)-1):

        if values[i] > values[i+1]:
            index = i+1
            in_order = False
            break

    return in_order, index
