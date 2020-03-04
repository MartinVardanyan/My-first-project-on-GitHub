class DateError(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_obj(self):
        print(self.a, self.b)


class Date:
    MD = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, day: int, month: int, year: int):
        try:
            if year <= 0:
                raise DateError('Your year must be a positive number:', year)
            else:
                self.__year = year
            if month <= 0:
                raise DateError("Your month must be a positive number:", month)
            elif month > 12:
                raise DateError("Wrong number for month:", month)
            else:
                self.__month = month
            if day <= 0:
                raise DateError("Wrong number for day, cant be a negative number:", day)
            elif self.__is_leap_year():
                raise DateError("Wrong number for day, this year is not leap year:", day)
            elif day > self.MD[self.__month - 1]:
                raise DateError("Wrong number for day:", day)
            elif day == 29 and self.__year % 400 != 0 and self.__year % 100 == 0:
                raise DateError("Wrong number for day, this year is not leap year:", day)
            elif day == 29 and self.__year % 4 != 0 and self.__year % 100 != 0 and self.__year % 400 != 0:
                raise DateError("Wrong number for day, this year is not leap year:", day)
            else:
                self.__day = day
        except DateError as e:
            e.print_obj()

    def __repr__(self):
        return "{}.{}.{}".format(self.__day, self.__month, self.__year)

    def get_day(self):
        return self.__day

    def set_day(self, value):
        try:
            if value <= 0:
                raise DateError("Wrong number for day, cant be a negative number:", value)
            elif value is self.__is_leap_year():
                raise DateError("Wrong number for day, this year is not leap year:", value)
            elif value > self.MD[self.__month - 1]:
                raise DateError("Wrong number for day, this year don`t have so many day:", value)
            else:
                self.__day = value
        except DateError as e:
            e.print_obj()

    def get_month(self):
        return self.__month

    def set_month(self, value):
        try:
            if value <= 0:
                raise DateError("Wrong number for month, cant be a negative number:", value)
            elif value == 2 and value != self.__is_leap_year() and self.__day > self.MD[1]:
                raise DateError("Wrong number for month, this year is not leap year:", value)
            elif value > 12:
                raise DateError("Wrong number for month:", value)
            else:
                self.__month = value
        except DateError as e:
            e.print_obj()

    def get_year(self):
        return self.__year

    def set_year(self, value):
        try:
            if value < 0:
                raise DateError("Wrong number for year, cant be a negative number:", value)
            elif value % 4 != 0 and self.__day == 29:
                raise DateError("Wrong number for year, not leap year:", value)
            elif value % 100 == 0 and value % 400 != 0:
                raise DateError("Wrong number for year, not leap year:", value)
            else:
                self.__year = value
        except DateError as e:
            e.print_obj()

    def add_month(self, month):
        try:
            if month <= 0:
                raise DateError("Wrong number for month, cant be a negative number:", month)
            else:
                m = self.__month + month
                self.add_year((m - 1) // 12)
                self.__month = (m - 1) % 12 + 1
        except DateError as e:
            e.print_obj()

    def __is_leap_year(self):
        if self.__year % 400 == 0:
            self.MD[1] = 29
        elif self.__year % 100 == 0:
            self.MD[1] = 28
        elif self.__year % 4 == 0:
            self.MD[1] = 29
        else:
            self.MD[1] = 28

    def add_year(self, year):
        try:
            if year < 0:
                raise DateError("Wrong number fo year, cant be a negative number:", year)
            else:
                y = self.__year + year
                self.__year = y
        except DateError as e:
            e.print_obj()

    def add_day(self, day):
        try:
            if day < 0:
                raise DateError("Wrong number for day, cant be a negative number:", day)
            else:
                d = self.__day + day
                while d > self.MD[self.__month - 1]:
                    d -= self.MD[self.__month - 1]
                    self.__is_leap_year()
                    self.add_month(1)
                self.__day = d
        except DateError as e:
            e.print_obj()
