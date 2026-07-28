import re


def is_isogram(phrase):
    letters = [letter.lower() for letter in phrase if letter.isalpha()]
    return len(letters) == len(set(letters))