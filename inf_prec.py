"""Base description of fraction class, based on infinite integer precision.
Basic functions used in fraction arithmetic operations like greatest common
divisor and lowest common denominator."""


def gcd(a: int, b: int) -> int:
    """Greatest common divisor, find highest number c such that
    a%c == b%c == 0"""
    a = abs(a)
    b = abs(b)
    if b > a:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a


def lcd(a: int, b: int) -> int:
    """Lowest common denominator, find lowest number c such that
    c%a == c%b == 0
        lcd(a,b) = ab/gcd(a, b)"""
    a = abs(a)
    b = abs(b)

    return (a // gcd(a, b)) * b


class Number:
    """Remember numerator and denominator, some functionalities about basic
    arithmethic operations."""
    def __init__(self, numerator, denominator=1, negative=False):
        if denominator == 0:
            raise ValueError("Denominator can not be zero.")
        if numerator < 0 or denominator < 0:
            raise ValueError("Values used must be positive, use sign bit\
                             instead.")
        self.numerator = numerator
        self.denominator = denominator
        self.negative = negative

    def __str__(self):
        return "{0}/{1} {2} {3}".format(self.numerator, self.denominator,
                                        self.negative,
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
            # Find lcd, calculate adjusted numerators and act accordingly.
            denominator = lcd(self.denominator, item.denominator)
            first = self.numerator * (denominator // self.denominator)
            second = item.numerator * (denominator // item.denominator)
            if not self.negative and item.negative:
                numerator = first - second
            elif self.negative and not item.negative:
                numerator = second - first
            else:
                numerator = first + second
            res = Number(abs(numerator), denominator)
            if numerator < 0 or self.negative and item.negative:
                res.negative = True

            res.reduce()
            return res

    def __sub__(self, item):
        if isinstance(item, Number):
            item.negative = not item.negative
            res = self.__add__(item)
            item.negative = not item.negative

            return res

    def __mul__(self, item):
        if isinstance(item, Number):
            res = Number(self.numerator * item.numerator,
                         self.denominator * item.denominator)
            res.reduce()
            res.negative = (self.negative or item.negative)
            return res

    def __truediv__(self, item):
        if isinstance(item, Number):
            res = Number(self.numerator * item.denominator,
                         self.denominator * item.numerator)
            res.reduce()
            res.negative = (self.negative or item.negative)
            return res

    def __pow__(self, item):
        if isinstance(item, int):
            res = Number(self.numerator ** item, self.denominator ** item)
            if item % 2 == 1 and self.negative:
                res.negative = True
            res.reduce()
            return res
