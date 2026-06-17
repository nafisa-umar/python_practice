"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the number of minutes required for preparing layers.
    
    :param number_of_layers: int - number of layers you want to add to the lasagna
    :return: int - preparation time (in minutes) derived from PREPARATION_TIME
    
    Function that takes the number of layers of the lasagna being prepared and returns        how  many minutes it would take to prepare the layers based on the
    PREPARATION_TIME(in minutes) per layer
    """
    
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total time(in minutes) spent cooking in the kitchen.

    :param number_of_layers: int - number of layers you want to add to the lasagna
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total time spent in the kitchen cooking.

    Function that takes the number of layers of the lasagna being prepared and baking         time to calculate total time spent in the kitchen
    """
    
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time