class MoneyError(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_obj(self):
        print(self.a, self.b)


class Money:
    exchange = {'AMD': 1, 'RUB': 8, 'USD': 480, 'EUR': 530}

    def __init__(self, am: int, cr: str):
        try:
            if am < 0:
                raise MoneyError("Amount cant be a negative number:", am)
            elif cr.upper() not in self.exchange.keys():
                raise MoneyError("Your currency must be one of this: RUB, EUR, USD or AMD:", cr)
            else:
                self.__amount = am
                self.__currency = cr.upper()
        except MoneyError as me:
            me.print_obj()

    def __repr__(self):
        return "{} {}".format(self.__amount, self.__currency)

    def set_amount(self, value):
        try:
            if value < 0:
                raise MoneyError("Amount cant be a negative number:", value)
            else:
                self.__amount = value
        except MoneyError as me:
            me.print_obj()

    def get_amount(self):
        return self.__amount

    def get_currency(self):
        return self.__currency

    def set_currency(self, value):
        try:
            if value in self.exchange.keys():
                raise MoneyError("Your currency must one of this: RUB, EUR, USD or AMD:", value)
            else:
                self.__currency = value
        except MoneyError as me:
            me.print_obj()

    def conversion(self, other):
        coefficient = self.exchange[self.__currency] / self.exchange[other.__currency]
        other.set_amount(self.get_amount() * coefficient)
        return Money(other.get_amount(), other.get_currency())

    def __add__(self, other):
        convert = (other.get_amount() * (self.exchange[other.get_currency()] / self.exchange[self.get_currency()]))
        end = convert + self.get_amount()
        return Money(end, self.get_currency())

    def __sub__(self, other):
        convert = (other.get_amount() * (self.exchange[other.get_currency()] / self.exchange[self.get_currency()]))
        end = self.get_amount() - convert
        return Money(end, self.get_currency())

    def __truediv__(self, other):
        convert = other.get_amount() * (self.exchange[other.get_currency()] / self.exchange[self.get_currency()])
        end = self.get_amount() / convert
        return end

    def __eq__(self, other):
        convert = other.get_amount() * (self.exchange[other.get_currency()] / self.exchange[self.get_currency()])
        if self.get_amount() == convert:
            return True
        return False

    def __ne__(self, other):
        convert = other.get_amount() * (self.exchange[other.get_currency()] / self.exchange[self.get_currency()])
        if self.get_amount() != convert:
            return True
        return False

    def __lt__(self, other):
        convert = other.get_amount() * (self.exchange[other.get_currency()] / self.exchange[self.get_currency()])
        if self.get_amount() < convert:
            return True
        return False

    def __gt__(self, other):
        convert = other.get_amount() * (self.exchange[other.get_currency()] / self.exchange[self.get_currency()])
        if self.get_amount() > convert:
            return True
        return False

    def __le__(self, other):
        convert = other.get_amount() * (self.exchange[other.get_currency()] / self.exchange[self.get_currency()])
        if self.get_amount() <= convert:
            return True
        return False

    def __ge__(self, other):
        convert = other.get_amount() * (self.exchange[other.get_currency()] / self.exchange[self.get_currency()])
        if self.get_amount() >= convert:
            return True
        return False
