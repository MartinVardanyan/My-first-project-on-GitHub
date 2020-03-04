from money_class import Money


def init_repr_test(am, cr):
    obj = Money(am, cr)
    print(obj)


def get_amount_test(am, cr):
    obj = Money(am, cr)
    print(obj.get_amount())


def set_amount_test(amount):
    obj = Money(100, 'USD')
    obj.set_amount(amount)
    print(obj)


def get_currency_test(am, cr):
    obj = Money(am, cr)
    print(obj.get_currency())


def set_currency_test(currency):
    obj = Money(100, 'USD')
    obj.set_currency(currency)
    print(obj)


def conversion_test(am1, cr1, am2, cr2):
    obj1 = Money(am1, cr1)
    other = Money(am2, cr2)
    obj2 = obj1.conversion(other)
    print(obj2)


def add_test(am1, cr1, am2, cr2):
    obj1 = Money(am1, cr1)
    obj2 = Money(am2, cr2)
    print(obj1 + obj2)


def sub_test(am1, cr1, am2, cr2):
    obj1 = Money(am1, cr1)
    obj2 = Money(am2, cr2)
    print(obj1 - obj2)


def truediv_test(am1, cr1, am2, cr2):
    obj1 = Money(am1, cr1)
    obj2 = Money(am2, cr2)
    print(obj1 / obj2)


def eq_test(am1, cr1, am2, cr2):
    obj1 = Money(am1, cr1)
    obj2 = Money(am2, cr2)
    print(obj1 == obj2)


def ne_test(am1, cr1, am2, cr2):
    obj1 = Money(am1, cr1)
    obj2 = Money(am2, cr2)
    print(obj1 != obj2)


def lt_test(am1, cr1, am2, cr2):
    obj1 = Money(am1, cr1)
    obj2 = Money(am2, cr2)
    print(obj1 < obj2)


def gt_test(am1, cr1, am2, cr2):
    obj1 = Money(am1, cr1)
    obj2 = Money(am2, cr2)
    print(obj1 > obj2)


def le_test(am1, cr1, am2, cr2):
    obj1 = Money(am1, cr1)
    obj2 = Money(am2, cr2)
    print(obj1 <= obj2)


def ge_test(am1, cr1, am2, cr2):
    obj1 = Money(am1, cr1)
    obj2 = Money(am2, cr2)
    print(obj1 >= obj2)


init_repr_test(700, 'usd')