from rational_class import Rational


def test_init_repr_gcd_normalization(nominator, denominator):
    obj = Rational(nominator, denominator)
    print(obj)


def test_get_nominator(nominator, denominator):
    obj = Rational(nominator, denominator)
    print(obj.get__nominator())


def test_set_nominator(nominator):
    obj = Rational(4, 5)
    obj.set__nominator(nominator)
    print(obj)


def test_get_denominator(nominator, denominator):
    obj = Rational(nominator, denominator)
    print(obj.get__denominator())


def test_set_denominator(denominator):
    obj = Rational(4, 5)
    obj.set_denominator(denominator)
    print(obj)


def test_add(n1, d1, n2, d2):
    obj1 = Rational(n1, d1)
    obj2 = Rational(n2, d2)
    print(obj1 + obj2)


def test_sub(n1, d1, n2, d2):
    obj1 = Rational(n1, d1)
    obj2 = Rational(n2, d2)
    print(obj1 - obj2)


def test_mul(n1, d1, n2, d2):
    obj1 = Rational(n1, d1)
    obj2 = Rational(n2, d2)
    print(obj1 * obj2)


def test_truediv(n1, d1, n2, d2):
    obj1 = Rational(n1, d1)
    obj2 = Rational(n2, d2)
    print(obj1 / obj2)


def test_eq(n1, n2, d1, d2):
    obj1 = Rational(n1, d1)
    obj2 = Rational(n2, d2)
    print(obj1 == obj2)


def test_ne(n1, n2, d1, d2):
    obj1 = Rational(n1, d1)
    obj2 = Rational(n2, d2)
    print(obj1 != obj2)


def test_lt(n1, n2, d1, d2):
    obj1 = Rational(n1, d1)
    obj2 = Rational(n2, d2)
    print(obj1 < obj2)


def test_gt(n1, n2, d1, d2):
    obj1 = Rational(n1, d1)
    obj2 = Rational(n2, d2)
    print(obj1 > obj2)


def test_le(n1, n2, d1, d2):
    obj1 = Rational(n1, d1)
    obj2 = Rational(n2, d2)
    print(obj1 <= obj2)


def test_ge(n1, n2, d1, d2):
    obj1 = Rational(n1, d1)
    obj2 = Rational(n2, d2)
    print(obj1 >= obj2)


def test_pow(nominator, denominator, power):
    obj1 = Rational(nominator ** power, denominator ** power)
    print(obj1)
