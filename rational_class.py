class RationalError(Exception):
    def __init__(self,a ,b):
        self.a = a
        self.b = b

    def print_obj(self):
        print(self.a, self.b)


class Rational:
    def __init__(self, a: int, b: int):
        try:
            if type(a) != int:
                raise RationalError("Wrong number for nominator, must be a integer:", a)
            elif type(b) != int:
                raise RationalError("Wrong number for denominator, must be a integer:", b)
            elif b == 0:
                raise RationalError("Wrong number for denominator, cant be a zero:", b)
            elif a < 0:
                raise RationalError("Wrong number for nominator, cant be a negative number:", a)
            elif b < 0:
                raise RationalError("Wrong number for denominator, cant be a negative number:", b)
            else:
                a, b = self.__normalization(a, b)
                self.__nominator = a
                self.__denominator = b
        except RationalError as rt:
            rt.print_obj()

    def __repr__(self):
        return "{}|{}".format(self.__nominator, self.__denominator)

    def set__nominator(self, value):
        try:
            if type(value) != int:
                raise RationalError("Wrong number for nominator, must be a integer:", value)
            elif value < 0:
                raise("Wrong number for nominator, cant be a negative number:", value)
            else:
                self.__nominator = value
        except RationalError as rt:
            rt.print_obj()

    def get__nominator(self):
        return self.__nominator

    def set_denominator(self, value):
        try:
            if type(value) != int:
                raise RationalError("Wrong number for denominator, must be a integer:", value)
            elif value <= 0:
                raise RationalError("Wrong number for denominator, cant be zero or negative number:", value)
            else:
                self.__denominator = value
        except RationalError as rt:
            rt.print_obj()

    def get__denominator(self):
        return self.__denominator

    def __normalization(self, a, b):
        z = self.__gcd(a, b)
        return a // z, b // z

    @staticmethod
    def __gcd(a, b):
        while a != 0 and b != 0:
            if a > b:
                a %= b
            else:
                b %= a
        return a + b

    def __add__(self, add):
        a = (self.__nominator * add.__denominator) + (self.__denominator * add.__nominator)
        b = self.__denominator * add.__denominator
        return Rational(a, b)

    def __sub__(self, sub):
        a = (self.__nominator * sub.__denominator) - (self.__denominator * sub.__nominator)
        b = self.__denominator * sub.__denominator
        return Rational(a, b)

    def __mul__(self, mul):
        a = self.__nominator * mul.__nominator
        b = self.__denominator * mul.__denominator
        return Rational(a, b)

    def __truediv__(self, div):
        a = self.__nominator * div.__denominator
        b = self.__denominator * div.__nominator
        return Rational(a, b)

    def __eq__(self, other):
        if self.__nominator == other.__nominator and self.__denominator == other.__denominator:
            return True
        return False

    def __ne__(self, other):
        if self.__nominator / self.__denominator != other.__nominator / other.__denominator:
            return True
        return False

    def __lt__(self, other):
        if self.__nominator / self.__denominator < other.__nominator / other.__denominator:
            return True
        return False

    def __gt__(self, other):
        if self.__nominator / self.__denominator > other.__nominator / other.__denominator:
            return True
        return False

    def __le__(self, other):
        if self.__nominator / self.__denominator <= other.__nominator / other.__denominator:
            return True
        return False

    def __ge__(self, other):
        if self.__nominator / self.__denominator >= other.__nominator / other.__denominator:
            return True
        return False

    def __pow__(self, power):
        self.__nominator = self.__nominator ** power
        self.__denominator = self.__denominator ** power
