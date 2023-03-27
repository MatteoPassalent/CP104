"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matteo Passalent
ID:      210597410
Email:   pass7410@mylaurier.ca
__updated__ = "2022-10-30"
-------------------------------------------------------
"""


def day_of_week(day_number):
    """
    -------------------------------------------------------
    Takes an integer parameter and returns a string representing 
    the corresponding day of the week, where 1 = "Monday", 
    2 = "Tuesday", up to 7 = "Sunday". The function returns "Error" 
    if the parameter is a number outside the range of 1 through 7
    Use: day = day_of_week(day_number)
    -------------------------------------------------------
    Parameters:
        day_number - day number of the week (int)
    Returns:
        day - name of the weekday (str)
    -------------------------------------------------------
    """

    if day_number == 1:
        day = "Monday"

    elif day_number == 2:
        day = "Tuesday"

    elif day_number == 3:
        day = "Wednesday"

    elif day_number == 4:
        day = "Thursday"

    elif day_number == 5:
        day = "Friday"

    elif day_number == 6:
        day = "Saturday"

    elif day_number == 7:
        day = "Sunday"

    else:
        day = "Error"

    return day


def pollution_level(aqi):
    """
    -------------------------------------------------------
    Returns the pollution level given an AQI (Air Quality Index):
        "Good" - 0 to 50 AQI
        "Moderate" - 51 - 100 AQI
        "Unhealthy for Sensitive Groups" - 101 - 150 AQI
        "Unhealthy" - 151 - 200 AQI
        "Very Unhealthy" - 201 - 300 AQI
        "Hazardous" - 300+ AQI
    Returns "Error" if aqi is negative.
    Use: level = pollution_level(aqi)
    -------------------------------------------------------
    Parameters:
        aqi - Air Quality Index (int)
    Returns:
        level - name of pollution level (str)
    ------------------------------------------------------
    """

    if aqi >= 300:
        level = "Hazardous"

    elif aqi >= 201:
        level = "Very Unhealthy"

    elif aqi >= 151:
        level = "Unhealthy"

    elif aqi >= 101:
        level = "Unhealthy for Sensitive Groups"

    elif aqi >= 51:
        level = "Moderate"

    elif aqi >= 0:
        level = "Good"

    else:
        level = "Error"

    return level


def product_largest(v1, v2, v3):
    """
    -------------------------------------------------------
    Returns the product of the two largest values of
    v1, v2, and v3.
    Use: product = product_largest(v1, v2, v3)
    -------------------------------------------------------
    Parameters:
        v1 - a number (float)
        v2 - a number (float)
        v3 - a number (float)
    Returns:
        product - the product of the two largest values of
            v1, v2, and v3 (float)
    ------------------------------------------------------
    """
    if v1 >= v3 and v2 >= v3:
        product = v1 * v2

    elif v1 >= v2 and v3 >= v2:
        product = v1 * v3

    elif v2 >= v1 and v3 >= v1:
        product = v2 * v3

    return product


def rgb_mix(rgb1, rgb2):
    """
    -------------------------------------------------------
    Determines the secondary colour from mixing two primary
    RGB (Red, Green, Blue) colours. The order of the colours
    is *not* significant.
    Returns "Error" if any of the colour parameter(s) are invalid.
        "red" + "blue": "fuchsia"
        "red" + "green": "yellow"
        "green" + "blue": "aqua"
        "red" + "red": "red"
        "blue" + "blue": "blue"
        "green" + "green": "green"
    Use: colour = rgb_mix(rgb1, rgb2)
    -------------------------------------------------------
    Parameters:
        rgb1 - a primary RGB colour (str)
        rgb2 - a primary RGB colour (str)
    Returns:
        colour - a secondary RGB colour (str)
    -------------------------------------------------------
    """
    if rgb1 == "red":

        if rgb2 == "red":
            colour = "red"

        elif rgb2 == "blue":
            colour = "fuchsia"

        elif rgb2 == "green":
            colour = "yellow"
        else:
            colour = "Error"

    elif rgb1 == "blue":

        if rgb2 == "red":
            colour = "fuchsia"

        elif rgb2 == "blue":
            colour = "blue"

        elif rgb2 == "green":
            colour = "aqua"

        else:
            colour = "Error"

    elif rgb1 == "green":

        if rgb2 == "red":
            colour = "yellow"

        elif rgb2 == "blue":
            colour = "aqua"

        elif rgb2 == "green":
            colour = "green"

        else:
            colour = "Error"

    else:
        colour = "Error"

    return colour


def yee_ha(number):
    """
    -------------------------------------------------------
    Takes an integer and returns one of the following:
    "Yee" if the number is divisible by 3
    "Ha" if the number is divisible by 7
    "Yee Ha" if the number is divisible by both 3 and 7
    "Nada" if it is neither divisible by 3 nor 7
    Use: feedback = yee_ha(number)
    -------------------------------------------------------
    Parameters:
    number - any real integer (int)
    Returns:
    response - does division tests listed above (str)
    -------------------------------------------------------
    """
    if number % 3 == 0 and number % 7 == 0:
        response = "Yee Ha"

    elif number % 3 == 0:
        response = "Yee"

    elif number % 7 == 0:
        response = "Ha"

    else:
        response = "Nada"

    return response
