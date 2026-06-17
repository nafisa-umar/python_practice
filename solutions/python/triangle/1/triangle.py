def is_triangle(sides):
    a, b, c = sides
    if (a + b >= c) and (b + c >= a) and (a + c >= b) and 0 not in sides:
        return True
    return False


def equilateral(sides):
    a = sides[0]
    if sides.count(a) == 3 and is_triangle(sides):
        return True
    return False


def isosceles(sides):
    a, b, c = sides
    check_1 = (a == b) or (a == c)
    check_2 = (b == a) or (b == c)
    check_3 = (c == a) or (c == b)
    if (check_1 or check_2 or check_3) and is_triangle(sides):
        return True
    return False


def scalene(sides):
    if is_triangle(sides) and not (isosceles(sides) or equilateral(sides)):
        return True
    return False