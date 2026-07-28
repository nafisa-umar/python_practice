import re


def is_isogram(phrase):
    letters = re.sub(r'[^a-zA-Z]', '', phrase)
    unique_letters = set(letters.lower())
    if len(letters) == len(unique_letters):
        return True
    return False