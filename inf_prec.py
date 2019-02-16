"""Base description of fraction class, based on infinite integer precision.
Basic functions used in fraction arithmetic operations like greatest common
divisor and lowest common denominator."""

# TODO: gcd and lcd with negative numbers, consider.


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
        if (c % a == 0 and
                c % b == 0):
            return c

    return maximum


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
        """Reduce fraction (divide by common divisor in numerator and
        denominator). """
        maximum = max(abs(self.numerator), abs(self.denominator))
        for val in range(maximum, 1, -1):
            if self.numerator % val == 0 == self.denominator % val:
                self.numerator //= val
                self.denominator //= val

    def __eq__(self, item):
        if isinstance(item, Number):
            self.reduce()
            item.reduce()
            if (self.numerator == item.numerator and
                    self.denominator == self.denominator):
                return True
        return False

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


a = Number(1, 2)
b = Number(1, 3)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
