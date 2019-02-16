"""Base description of fraction class, based on infinite integer precision.
Basic functions used in fraction arithmetic operations like greatest common
divisor and lowest common denominator."""

# TODO: gcd and lcd with negative numbers, consider.

import cProfile


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
    c%a == c%b == 0
        lcd(a,b) = ab/gcd(a, b)"""

    return (a // gcd(a, b)) * b


class Number:
    """Remember numerator and denominator, some functionalities about basic
    arithmethic operations."""
    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ValueError("Denominator can not be zero.")
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return "{0}/{1} {2}".format(self.numerator, self.denominator,
                                    self.numerator / self.denominator)

    def reduce(self):
        """Reduce fraction (divide by greatest common divisor in numerator and
        denominator). """
        reducer = gcd(self.numerator, self.denominator)

        self.numerator //= reducer
        self.denominator //= reducer

    def __eq__(self, item):
        if isinstance(item, Number):
            self.reduce()
            item.reduce()
            if (self.numerator == item.numerator and
                    self.denominator == self.denominator):
                return True
        return False

    def __gt__(self, item):
        if isinstance(item, Number):
            # Find common denominator and compare adjusted numerators.
            denominator = lcd(self.denominator, item.denominator)
            first = self.numerator * (denominator // self.denominator)
            second = item.numerator * (denominator // item.denominator)
            return first > second

    def __add__(self, item):
        if isinstance(item, Number):
            denominator = lcd(self.denominator, item.denominator)
            res = Number(self.numerator * (denominator // self.denominator) +
                         item.numerator * (denominator // item.denominator),
                         denominator)
            res.reduce()
            return res

    def __sub__(self, item):
        if isinstance(item, Number):
            denominator = lcd(self.denominator, item.denominator)
            res = Number(self.numerator * (denominator // self.denominator) -
                         item.numerator * (denominator // item.denominator),
                         denominator)
            res.reduce()
            return res

    def __mul__(self, item):
        if isinstance(item, Number):
            res = Number(self.numerator * item.numerator,
                         self.denominator * item.denominator)
            res.reduce()
            return res

    def __truediv__(self, item):
        if isinstance(item, Number):
            res = Number(self.numerator * item.denominator,
                         self.denominator * item.numerator)
            res.reduce()
            return res


def main():
    a = Number(1, 2)
    b = Number(1, 3)
    print(a)
    print(b)
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)

    print()
    print()
    print()

    one = Number(1)
    two = Number(2)
    eps = Number(1)

    while one + eps/two > one:
        eps /= two
        print(eps)
    print(eps)


cProfile.run('main()')
