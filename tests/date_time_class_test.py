from date_time_class import DateTime
from date_class import Date
from time_class import Time


def test_init_repr(day, month, year, hour, minute, second):
    date = Date(day, month, year)
    time = Time(hour, minute, second)
    obj1 = DateTime(date, time)
    print(obj1)


def test_get_date(day, month, year, hour, minute, second):
    date = Date(day, month, year)
    time = Time(hour, minute, second)
    obj = DateTime(date, time)
    print(obj.get_date())


def test_set_date(day, month, year, hour, minute, second, setday, setmonth, setyear):
    date = Date(day, month, year)
    time = Time(hour, minute, second)
    obj = DateTime(date, time)
    obj.set_date(setday, setmonth, setyear)
    print(obj)


def test_get_time(day, month, year, hour, minute, second):
    date = Date(day, month, year)
    time = Time(hour, minute, second)
    obj = DateTime(date, time)
    print(obj.get_time())


def test_set_time(day, month, year, hour, minute, second, sethour, setminute, setsecond):
    date = Date(day, month, year)
    time = Time(hour, minute, second)
    obj = DateTime(date, time)
    obj.set_time(sethour, setminute, setsecond)
    print(obj)


def test_add_year(day, month, year, hour, minute, second, addyear):
    date = Date(day, month, year)
    time = Time(hour, minute, second)
    obj = DateTime(date, time)
    obj.add_year(addyear)
    print(obj)


def test_add_month(day, month, year, hour, minute, second, addmonth):
    date = Date(day, month, year)
    time = Time(hour, minute, second)
    obj = DateTime(date, time)
    obj.add_month(addmonth)
    print(obj)


def test_add_day(day, month, year, hour, minute, second, addday):
    date = Date(day, month, year)
    time = Time(hour, minute, second)
    obj = DateTime(date, time)
    obj.add_day(addday)
    print(obj)


def test_add_hour(day, month, year, hour, minute, second, addhour):
    date = Date(day, month, year)
    time = Time(hour, minute, second)
    obj = DateTime(date, time)
    obj.add_hour(addhour)
    print(obj)


def test_add_minute(day, month, year, hour, minute, second, addminute):
    date = Date(day, month, year)
    time = Time(hour, minute, second)
    obj = DateTime(date, time)
    obj.add_minute(addminute)
    print(obj)


def test_add_second(day, month, year, hour, minute, second, addsecond):
    date = Date(day, month, year)
    time = Time(hour, minute, second)
    obj = DateTime(date, time)
    obj.add_second(addsecond)
    print(obj)


def test_add_h_m_s(day, month, year, hour, minute, second, addhour, addminute, addsecond):
    date = Date(day, month, year)
    time = Time(hour, minute, second)
    obj = DateTime(date, time)
    obj.add_hour(addhour)
    obj.add_minute(addminute)
    obj.add_second(addsecond)
    print(obj)


def test_add_d_m_y(day, month, year, hour, minute, second, adday, addmonth, addyear):
    date = Date(day, month, year)
    time = Time(hour, minute, second)
    obj = DateTime(date, time)
    obj.add_day(adday)
    obj.add_month(addmonth)
    obj.add_year(addyear)
    print(obj)


