class TimeError(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_obj(self):
        print(self.a, self.b)


class Time:
    def __init__(self, hour, minute, second):
        try:
            if hour < 0:
                raise TimeError("Hour must be a positive number:", hour)
            elif hour >= 24:
                raise TimeError("Wrong number for hour:", hour)
            elif minute < 0:
                raise TimeError("Minute must be a positive number:", minute)
            elif minute >= 60:
                raise TimeError("Wrong number for minute:", minute)
            elif second < 0:
                raise TimeError("Second must be a positive number:", second)
            elif second >= 60:
                raise TimeError("Wrong number for second:", second)
            else:
                self.__hour = hour
                self.__minute = minute
                self.__second = second
        except TimeError as t:
            t.print_obj()

    def __repr__(self):
        return "{}:{}:{}".format(self.__hour, self.__minute, self.__second)

    def set_second(self, value):
        try:
            if value < 0:
                raise TimeError("Your second must be a positive number:", value)
            elif value >= 60:
                raise TimeError("Wrong number for second:", value)
            else:
                self.__second = value
        except TimeError as t:
            t.print_obj()

    def get_second(self):
        return self.__second

    def set_minute(self, value):
        try:
            if value < 0:
                raise TimeError("Your minute must be positive number:", value)
            elif value >= 60:
                raise TimeError("Wrong number for minute:", value)
            else:
                self.__minute = value
        except TimeError as t:
            t.print_obj()

    def get_minute(self):
        return self.__minute

    def get_hour(self):
        return self.__hour

    def set_hour(self, value):
        try:
            if value < 0:
                raise TimeError("Your hour must be a positive number:", value)
            elif value >= 24:
                raise TimeError("Wrong number for hour:", value)
            else:
                self.__hour = value
        except TimeError as t:
            t.print_obj()

    def add_hour(self, hour):
        try:
            if hour < 0:
                raise TimeError("Your hour must be a positive number:", hour)
            else:
                self.__hour = (self.__hour + hour) % 24
        except TimeError as t:
            t.print_obj()

    def add_minute(self, minute):
        try:
            if minute < 0:
                raise TimeError("Your minute must be a positive number:", minute)
            else:
                w = self.__minute + minute
                if w >= 60:
                    s = w // 60
                    self.add_hour(s)
                self.__minute = w % 60
        except TimeError as t:
            t.print_obj()

    def add_second(self, second):
        try:
            if second < 0:
                raise TimeError("Your second must be a positive number:", second)
            else:
                q = self.__second + second
                if q >= 60:
                    r = q // 60
                    self.add_minute(r)
                self.__second = q % 60
        except TimeError as t:
            t.print_obj()
