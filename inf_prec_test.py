from . import inf_prec

# Greatest common divisor.


def test_gcd_a_bigger_than_b():
    assert inf_prec.gcd(12, 8) == 4
    assert inf_prec.gcd(12, 5) == 1
    assert inf_prec.gcd(16, 8) == 8


def test_gcd_a_lower_than_b():
    assert inf_prec.gcd(8, 12) == 4
    assert inf_prec.gcd(5, 12) == 1
    assert inf_prec.gcd(8, 16) == 8


def test_gcd_a_equals_b():
    assert inf_prec.gcd(12, 12) == 12
    assert inf_prec.gcd(3, 3) == 3
    assert inf_prec.gcd(7, 7) == 7


def test_gcd_negatives():
    assert inf_prec.gcd(12, -12) == 12
    assert inf_prec.gcd(3, -3) == 3
    assert inf_prec.gcd(-7, 7) == 7

# Lowest common denominator.


def test_lcd_a_bigger_than_b():
    assert inf_prec.lcd(12, 8) == 24
    assert inf_prec.lcd(13, 8) == 104
    assert inf_prec.lcd(9, 8) == 72


def test_lcd_a_lower_than_b():
    assert inf_prec.lcd(8, 12) == 24
    assert inf_prec.lcd(8, 13) == 104
    assert inf_prec.lcd(8, 9) == 72


def test_lcd_a_equals_b():
    assert inf_prec.lcd(12, 12) == 12
    assert inf_prec.lcd(13, 13) == 13
    assert inf_prec.lcd(9, 9) == 9


def test_lcd_negatives():
    assert inf_prec.lcd(8, -12) == 24
    assert inf_prec.lcd(-8, 13) == 104
    assert inf_prec.lcd(8, -9) == 72


# Reduce fractions.


def test_numerator_bigger_than_denominator():
    a = inf_prec.Number(12, 6)
    a.reduce()
    assert a == inf_prec.Number(2, 1)

    b = inf_prec.Number(9, 3)
    b.reduce()
    assert b == inf_prec.Number(3, 1)

    b = inf_prec.Number(9, 3, True)
    b.reduce()
    assert b == inf_prec.Number(3, 1, True)


def test_numerator_smaller_than_denominator():
    a = inf_prec.Number(6, 12)
    a.reduce()
    assert a == inf_prec.Number(1, 2)

    b = inf_prec.Number(3, 9)
    b.reduce()
    assert b == inf_prec.Number(1, 3)

    b = inf_prec.Number(3, 9, True)
    b.reduce()
    assert b == inf_prec.Number(1, 3, True)


def test_numerator_equals_denominator():
    a = inf_prec.Number(12, 12)
    a.reduce()
    assert a == inf_prec.Number(1, 1)

    b = inf_prec.Number(9, 9)
    b.reduce()
    assert b == inf_prec.Number(1, 1)

    b = inf_prec.Number(3, 3, True)
    b.reduce()
    assert b == inf_prec.Number(1, 1, True)


def test_add():
    a = inf_prec.Number(1, 2)
    b = inf_prec.Number(1, 3)
    assert a + b == inf_prec.Number(5, 6)


def test_add_negative():
    a = inf_prec.Number(1, 2)
    b = inf_prec.Number(1, 3, True)
    assert a + b == inf_prec.Number(1, 6)


def test_add_negatives():
    a = inf_prec.Number(1, 2, True)
    b = inf_prec.Number(1, 3, True)
    assert a + b == inf_prec.Number(5, 6, True)


def test_sub():
    a = inf_prec.Number(1, 2)
    b = inf_prec.Number(1, 3)
    assert a - b == inf_prec.Number(1, 6)


def test_sub_negative():
    a = inf_prec.Number(1, 2)
    b = inf_prec.Number(1, 3, True)
    assert a - b == inf_prec.Number(5, 6)


def test_sub_negatives():
    a = inf_prec.Number(1, 2, True)
    b = inf_prec.Number(1, 3, True)
    assert a - b == inf_prec.Number(1, 6, True)


def test_mul():
    a = inf_prec.Number(1, 2)
    b = inf_prec.Number(1, 3)
    assert a * b == inf_prec.Number(1, 6)


def test_mul_negative():
    a = inf_prec.Number(1, 2)
    b = inf_prec.Number(1, 3, True)
    assert a * b == inf_prec.Number(1, 6, True)


def test_mul_negatives():
    a = inf_prec.Number(1, 2, True)
    b = inf_prec.Number(1, 3, True)
    assert a * b == inf_prec.Number(1, 6)


def test_div():
    a = inf_prec.Number(1, 2)
    b = inf_prec.Number(1, 3)
    assert a / b == inf_prec.Number(3, 2)


def test_div_negative():
    a = inf_prec.Number(1, 2)
    b = inf_prec.Number(1, 3, True)
    assert a / b == inf_prec.Number(3, 2, True)


def test_div_negatives():
    a = inf_prec.Number(1, 2, True)
    b = inf_prec.Number(1, 3, True)
    assert a / b == inf_prec.Number(3, 2)


def test_pow():
    a = inf_prec.Number(1, 2)
    assert a ** 3 == inf_prec.Number(1, 8)

    b = inf_prec.Number(1, 2, True)
    assert b ** 3 == inf_prec.Number(1, 8, True)
