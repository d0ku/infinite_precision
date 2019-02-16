from . import inf_prec


def test_gcd_a_bigger_than_b():
    assert inf_prec.gcd(12, 8) == 4
    assert inf_prec.gcd(12, 5) == 1
    assert inf_prec.gcd(16, 8) == 8


def test_gcd_b_bigger_than_a():
    assert inf_prec.gcd(8, 12) == 4
    assert inf_prec.gcd(5, 12) == 1
    assert inf_prec.gcd(8, 16) == 8


def test_gcd_a_equals_b():
    assert inf_prec.gcd(12, 12) == 12
    assert inf_prec.gcd(3, 3) == 3
    assert inf_prec.gcd(7, 7) == 7
