from time_class import Time


def test_add_second(h, m, s, second):
    obj = Time(h, m, s)
    obj.add_second(second)
    print(obj)


def test_add_minute(h, m, s, minute):
    obj = Time(h, m, s)
    obj.add_minute(minute)
    print(obj)


def test_add_hour(h, m, s, hour):
    obj = Time(h, m, s)
    obj.add_hour(hour)
    print(obj)


def test_add_h_m_s(h, m, s, hour, minute, second):
    obj = Time(h, m, s)
    obj.add_second(second)
    obj.add_minute(minute)
    obj.add_hour(hour)
    print(obj)


def test_init_repr_time(hour, minute, second):
    obj = Time(hour, minute, second)
    print(obj)


def test_set_second(second):
    obj = Time(00, 00, 00)
    obj.set_second(second)
    print(obj)


def test_get_second(h, m, s):
    obj = Time(h, m, s)
    print(obj.get_second())


def test_set_minute(minute):
    obj = Time(00, 00, 00)
    obj.set_minute(minute)
    print(obj)


def test_get_minute(h, m, s):
    obj = Time(h, m, s)
    print(obj.get_minute())


def test_set_hour(hour):
    obj = Time(00, 00, 00)
    obj.set_hour(hour)
    print(obj)


def test_get_hour(h, m, s):
    obj = Time(h, m, s)
    print(obj.get_hour())
