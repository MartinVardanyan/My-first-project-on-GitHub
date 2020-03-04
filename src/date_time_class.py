from time_class import Time
from date_class import Date


class DateTimeError(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_obj(self):
        print(self.a, self.b)


class DateTime:
    def __init__(self, d, t):
        self.__date = d
        self.__time = t

    def __repr__(self):
        return "{} {}".format(self.__date, self.__time)

    def set_date(self, d, m, y):
        try:
            if d <= 0 or d > 28 and m == 2 or d > 30 and m == 4 or d > 30 and m == 6 or d > 30 and m == 9 or d > 30 and m == 11 or d > 31 and m == 1 or d > 31 and m == 3 or d > 31 and m == 5 or d > 31 and m == 7 or d > 31 and m == 8 or d > 31 and m == 10 or d >31 and m == 12:
                raise DateTimeError('Wrong number for day, this month don`t have so many days:', d)
            elif m <= 0 or m > 12:
                raise DateTimeError("Wrong number for month:", m)
            elif y <= 0:
                raise DateTimeError("Wrong number for year, cant be a negative number:", y)
            else:
                self.__date = d, m, y
        except DateTimeError as dt:
            dt.print_obj()

    def get_date(self):
        return self.__date

    def set_time(self, h, m, s):
        try:
            if h <= 0 or h >= 24:
                raise DateTimeError("Wrong number for hour:", h)
            elif m >= 60 or m <= 0:
                raise DateTimeError("Wrong number for minute:", m)
            elif s >= 60 or s <= 0:
                raise DateTimeError("Wrong number for second:", s)
            else:
                self.__time = h, m, s
        except DateTimeError as dt:
            dt.print_obj()

    def get_time(self):
        return self.__time

    def add_year(self, year):
        try:
            if year < 0:
                raise DateTimeError("Wrong number for year, cant be a negative number:", year)
            else:
                self.__date.add_year(year)
        except DateTimeError as dt:
            dt.print_obj()

    def add_month(self, month):
        try:
            if month < 0:
                raise DateTimeError("Wrong number for month, cant be a negative number:", month)
            else:
                self.__date.add_month(month)
        except DateTimeError as dt:
            dt.print_obj()

    def add_day(self, day):
        try:
            if day < 0:
                raise DateTimeError("Wrong number for day, cant be a negative number:", day)
            else:
                self.__date.add_day(day)
        except DateTimeError as dt:
            dt.print_obj()

    def add_hour(self, hour):
        try:
            if hour < 0:
                raise DateTimeError("Wrong number for hour, cant be a negative number:", hour)
            else:
                time = self.__time.get_hour() + hour
                if time >= 24:
                    self.__time.set_hour(time % 24)
                    self.add_day(time // 24)
                else:
                    self.__time.set_hour(time)
        except DateTimeError as dt:
            dt.print_obj()

    def add_minute(self, minute):
        try:
            if minute < 0:
                raise DateTimeError("Wrong number for minute, cant be a negative number:", minute)
            else:
                time = self.__time.get_minute() + minute
                if time >= 60:
                    self.__time.set_minute(time % 60)
                    self.add_hour(time // 60)
                else:
                    self.__time.set_minute(time)
        except DateTimeError as dt:
            dt.print_obj()

    def add_second(self, second):
        try:
            if second < 0:
                raise DateTimeError("Wrong number for second, cant be a negative number:", second)
            else:
                time = self.__time.get_second() + second
                if time >= 60:
                    self.__time.set_second(time % 60)
                    self.add_minute(time//60)
                else:
                    self.__time.set_second(time)
        except DateTimeError as dt:
            dt.print_obj()

'''d = Date(15, 10, 2020)
t = Time(14, 30, 47)
w = DateTime(d, t)
print(w)
w.add_second(12)
print(w)
w.add_minute(29)
print(w)
w.add_hour(9)
print(w)
w.add_day(16)
print(w)
w.add_month(2)
print(w)
w.add_second(1)
print(w)'''
