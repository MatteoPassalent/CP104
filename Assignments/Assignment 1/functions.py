"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matteo Passalent
ID:      210597410
Email:   pass7410@mylaurier.ca
__updated__ = "2023-01-22"
-------------------------------------------------------
"""


def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """

    count = 0

    values.reverse()

    for value in values:

        count = 0

        for i in values:

            if value == i:

                count += 1

        if count > 1:

            for _ in range(count-1):

                values.remove(value)

    values.reverse()


def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged.
    Use: u, l, d, w, r = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        u - the number of uppercase letters in the file (int)
        l - the number of lowercase letters in the file (int)
        d - the number of digits in the file (int)
        w - the number of whitespace characters in the file (int)
        r - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """

    u = 0
    l = 0
    d = 0
    w = 0
    r = 0

    file = fv.read()

    for char in file:

        if char.isupper():
            u += 1

        elif char.islower():
            l += 1

        elif char.isdigit():
            d += 1

        elif char.isspace():
            w += 1

        else:
            r += 1

    return u, l, d, w, r


def find_subs(string, sub):
    """
    -------------------------------------------------------
    Finds the indices of the locations of sub within string,
        left to right.
    Use: locations = find_subs(string, sub)
    -------------------------------------------------------
    Parameters:
        string - a string to evaluate (str)
        sub - a substring to locate in string (str)
    Returns:
        locations - an ordered list of the indices of the locations
            of sub within string (list of int)
    -------------------------------------------------------
    """

    locations = []
    count = string.count(sub)
    oc = string.index(sub)
    locations.append(oc)

    for i in range(count-1):

        start = len(string[:oc]) + len(sub)
        new_oc = string[oc + len(sub):].index(sub)

        oc = start + new_oc

        locations.append(oc)

    return locations


def is_leap_year(year):
    """
    -------------------------------------------------------
    Leap year determination.
    Use: leap_year = is_leap_year(year)
    -------------------------------------------------------
    Parameters:
        year - year to determine if it is a leap year (int > 0)
    Returns:
        leap_year - True if year is a leap year, False otherwise (boolean)
    -------------------------------------------------------
    """

    leap_year = False

    if year % 4 == 0 and year % 100 != 0:
        leap_year = True

    elif year % 100 == 0 and year % 400 == 0:
        leap_year = True

    return leap_year


def is_valid(name):
    """
    -------------------------------------------------------
    Determines if name is a valid Python variable name.
    Variables names must start with a letter or an underscore.
    The rest of the variable name may consist of letters, numbers
    and underscores.
    Use: valid = is_valid(name)
    -------------------------------------------------------
    Parameters:
        name - a string to test as a Python variable name (str)
    Returns:
        valid - True if name is a valid Python variable name,
            False otherwise (boolean)
    -------------------------------------------------------
    """

    valid = True

    if not name[0].isalpha() and name[0] != '_':
        valid = False
        print("one")

    for i in name:

        if not i.isalpha() and not i.isdigit() and i != '_':
            valid = False
            print("two")

    return valid


def matrix_transpose(a):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    Use: b = matrix_transpose(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (list of lists of ?)
    Returns:
        b - the transposed matrix (list of lists of ?)
    -------------------------------------------------------
    """

    for i in a:
        for j in i:
            b[j].append()
