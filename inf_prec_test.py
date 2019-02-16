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

# Reduce fractions.


def test_numerator_bigger_than_denominator():
    a = inf_prec.Number(12, 6)
    a.reduce()
    assert a == inf_prec.Number(2, 1)

    b = inf_prec.Number(9, 3)
    b.reduce()
    assert b == inf_prec.Number(3, 1)
