"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matteo Passalent
ID:      210597410
Email:   pass7410@mylaurier.ca
__updated__ = "2022-11-14"
-------------------------------------------------------
"""


def winner():
    """
    ---------------------------------------------------
    counts number of time winner occurs
    use: winner()
    ---------------------------------------------------
    Parameters: 
        None
    Returns:
        blue, grey
    ---------------------------------------------------
    """

    blue = 0
    grey = 0
    win = input('Enter the winning team: ')
    while win != "":
        if win == 'blue':
            blue = blue + 1
            win = input('Enter the winning team: ')
        elif win == 'grey':
            grey = grey + 1
            win = input('Enter the winning team: ')

    return blue, grey


def is_prime(num):
    """
    -------------------------------------------------------
    Determines if num is a prime number.
    Use: prime = is_prime(num)
    -------------------------------------------------------
    Parameters:
        num - a positive integer (int > 1)
    Returns:
        prime - True if num is prime, False otherwise (bool)
    ------------------------------------------------------
    """
    result = True
    count = 2
    while result == True and count < num:
        if num % count == 0:
            result = False
        else:
            count = count + 1

    return result


def interest_table(principal, rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal, rate, payment)
    -------------------------------------------------------
    Parameters:
        principal - original value of a loan (float > 0)
        rate - yearly interest rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """

    print('----------------------------------')
    print(f'Principal:   ${principal:0.00f}')
    print(f'Interest rate : {rate:0.0f}%')
    print(f'Monthly Payment: ${payment:0.00f}')
    print('----------------------------------')
    print(f'Month Interest   Payment   Balance')
    print('----------------------------------')

    month = 0
    interest = None
    while principal > 0:
        if principal > payment:
            interest = ((rate / 100) * principal)/12
            principal = principal - payment + interest
            month += 1
        else:
            month += 1
            interest = ((rate / 100) * principal)/12
            payment = principal + interest
            principal = 0

        print(f'{month:5d}{interest:10.2f}{payment:10.2f}{principal:12.2f}')

    return


def digit_count(num):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: count = digit_count(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int)
    Returns:
        count - the number of digits in num (int)
    ------------------------------------------------------
    """

    count = 1
    while abs(num) >= 10:

        num = num / 10
        count += 1

    return count


def sum_factors(num):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = sum_factors(num)
    -------------------------------------------------------
    Parameters:
        num - a positive integer (int >= 1)
    Returns:
        total - the total of num's factors (int)
    ------------------------------------------------------
    """

    div = 1
    count = 0
    while num//2 >= div:
        if num % div == 0:
            count = count + div
        div = div + 1

    return count
