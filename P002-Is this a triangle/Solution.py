def is_triangle(a, b, c):
    if (a + b <= c or b + c <= a or c + a <= b):
        return False
    return True
