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


def add_spaces(string):
    """
    -------------------------------------------------------
    Create a new string with added space between words. Words start
    with upper-case characters.
    Use: new_string = add_spaces(string)
    -------------------------------------------------------
    Parameters:
        string - string that represents a sentence in which all the
            words are run together (no spaces), but the first character
            of each word is uppercase. string has at least one
            character (str)
    Returns:
        new_string - new string in which the words are separated
            by spaces and only the first word starts with
            an uppercase character (str)
    -------------------------------------------------------
    """

    new_string = ''

    new_string = string[0].upper()

    for i in range(1, len(string)):

        if string[i].isupper():

            new_string += " "

        new_string += string[i].lower()

    return new_string


def pluralize(string):
    """
    -------------------------------------------------------
    Pluralizes a string according to the rules:
        - if string ends with 's', 'sh', or 'ch', add 'es'
        - if string ends with 'y' but not 'ay' or 'oy', replace
            the 'y' with 'ies'
        - otherwise add 's'
    Use: plural = pluralize(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        plural - a plural version of string (str)
    -------------------------------------------------------
    """

    plural = ''

    if string.endswith('s') or string.endswith('sh') or string.endswith('ch'):
        plural = string + 'es'

    elif string.endswith('y') and not string.endswith('ay') and not string.endswith('oy'):
        plural = string.rstrip('y')
        plural = plural + 'ies'

    else:
        plural = string + 's'

    return plural


def common_ending(string1, string2):
    """
    -------------------------------------------------------
    Returns the longest common ending of two strings.
    Use: common = common_ending(string1, string2)
    -------------------------------------------------------
    Parameters:
        string1 - first string for ending comparison (str)
        string2 - second string for ending comparison (str)
    Returns:
        common - the longest common ending of string1 and string2 (str)
    -------------------------------------------------------
    """

    count1 = None
    count2 = None
    common = ''

    for i in range(len(string1)):

        count1 = len(string1) - 1 - i
        count2 = len(string2) - 1 - i

        if string1[count1:] == string2[count2:]:
            common = string1[count1:]

    return common


def is_valid_isbn(isbn):
    """
    -------------------------------------------------------
    Determines if an ISBN string is valid. An ISBN string is valid if:
        - it consists of only digits and dashes ('-')
        - it contains 5 groups of digits separated by dashes
        - its first group of digits is either '978' or '979'
        - its final group of digits is a single digit
        - its entire length is 17 characters
    Use: valid = is_valid_isbn(isbn)
    -------------------------------------------------------
    Parameters:
        isbn - a string (str)
    Returns:
        valid - True if isbn is valid, False otherwise (boolean)
    -------------------------------------------------------
    """

    valid = True
    groups = isbn.split('-')

    if len(groups[4]) != 1:
        valid = False

    if len(groups) != 5:
        valid = False

    if len(isbn) != 17:
        valid = False

    if not isbn.startswith('978') and not isbn.startswith('979'):
        valid = False

    for i in groups:
        if not i.isdigit():
            valid = False

    return valid


def is_word_chain(word_list):
    """
    -------------------------------------------------------
    Determines if a list of strings is a word chain. A word chain
    is a list of words in which the last character of a word in
    the list is the same as the first character of the next word
    in the list.
    Use: word_chain = is_word_chain(word_list)
    -------------------------------------------------------
    Parameters:
        word_list - a of strings (list of str, len > 1)
    Returns:
        word_chain - True if word_list is a word chain,
            False otherwise (boolean)
    -------------------------------------------------------
    """

    word_chain = True
    last_character = word_list[0][-1]
    i = 1

    while word_chain and i < len(word_list):

        if word_list[i][0] != last_character:

            word_chain = False

        last_character = word_list[i][-1]
        i += 1

    return word_chain
