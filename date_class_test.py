from date_class import Date


def test_init_repr(day, month, year):
    obj = Date(day, month, year)
    print(obj)


def test_get_day(d, m, y):
    obj = Date(d, m, y)
    print(obj.get_day())


def test_set_day(d, m, y, day):
    obj = Date(d, m, y)
    obj.set_day(day)
    print(obj)


def test_get_month(d, m, y):
    obj = Date(d, m, y)
    print(obj.get_month())


def test_set_month(d, m, y, month):
    obj = Date(d, m, y)
    obj.set_month(month)
    print(obj)


def test_get_year(d, m, y):
    obj = Date(d, m, y)
    print(obj.get_year())


def test_set_year(d, m, y, year):
    obj = Date(d, m, y)
    obj.set_year(year)
    print(obj)


def test_add_day(d, m, y, day):
    obj = Date(d, m, y)
    obj.add_day(day)
    print(obj)


def test_add_month(d, m, y, month):
    obj = Date(d, m, y)
    obj.add_month(month)
    print(obj)


def test_add_year(d, m, y, year):
    obj = Date(d, m, y)
    obj.add_year(year)
    print(obj)


def test_add_d_m_y(d, m, y, day, month, year):
    obj = Date(d, m, y)
    obj.add_day(day)
    obj.add_month(month)
    obj.add_year(year)
    print(obj)


def test_leap_year(year):
    obj = Date(29, 2, year)
    print(obj)
