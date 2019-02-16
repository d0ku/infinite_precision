"""Base description of fraction class, based on infinite integer precision.
Basic functions used in fraction arithmetic operations like greatest common
divisor and lowest common denominator."""


def gcd(a: int, b: int) -> int:
    """Greatest common divisor, find highest number c such that
    a%c == b%c == 0"""
    if b > a:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a


def lcd(a: int, b: int) -> int:
    """Lowest common denominator, find lowest number c such that
    c%a == c%b == 0"""
    minimum = max(a, b)
    maximum = a*b

    for c in range(minimum, maximum+1):
        if c % a == c % b == 0:
            return c

    return maximum


class Number:
    """Remember numerator and denominator, some functionalities about basic
    arithmethic operations."""
    def __init__(self, numerator, denominator=0):
        self.numerator = numerator
        self.denominator = denominator
