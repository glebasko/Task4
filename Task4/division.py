"""

>>> divide(10, 2)
5.0

>>> divide(-10, 2)
-5.0

>>> divide(10, -2)
-5.0

>>> divide(0, 10)
0.0


>>> divide(10, 0)
Traceback (most recent call last):
    ...
ValueError: divisor can't be 0


>>> divide(1e100, 1)
Traceback (most recent call last):
    ...
OverflowError: dividend is too large


divide(1, 1e100)
Traceback (most recent call last):
    ...
OverflowError: divisor is too large

"""

def divide(dividend, divisor):
    import math

    if divisor == 0:
        raise ValueError("divisor can't be 0")
    if dividend+1 == dividend:
        raise OverflowError("dividend is too large")
    if divisor+1 == divisor:
        raise OverflowError("divisor is too large")

    result = dividend / divisor
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
