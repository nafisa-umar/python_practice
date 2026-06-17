def is_armstrong_number(number):
 
    digits = list(str(number))
    digits = [int(digit) for digit in digits]
    total_sum = 0

    for digit in digits:
        total_sum += digit ** len(digits)
    if total_sum == number:
        return True

    return False




