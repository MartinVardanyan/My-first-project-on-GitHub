class PersonError(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_obj(self):
        print(self.a, self.b)


class Person:
    def __init__(self, name: str, surname: str, age: int, gender: str):
        try:
            if age <= 0:
                raise PersonError("Person age cant be a negative number:", age)
            elif type(age) != int:
                raise PersonError("Person age must be a integer:", age)
            elif type(name) != str:
                raise PersonError("Person name must be a string:", name)
            elif type(surname) != str:
                raise PersonError("Person surname must be a string:", surname)
            elif type(gender) != str:
                raise PersonError("Person gender Male or Female:", gender)
            else:
                self.__name = name
                self.__surname = surname
                self.__age = age
                self.__gender = gender
        except PersonError as pe:
            pe.print_obj()

    def __repr__(self):
        return "{} {} - {} {}".format(self.__name, self.__surname, self.__age, self.__gender)

    def get_name(self):
        return self.__name

    def set_name(self, other):
        try:
            if type(other) != str:
                raise PersonError("Person name must be a string:", other)
            else:
                self.__name = other
        except PersonError as pe:
            pe.print_obj()

    def get_surname(self):
        return self.__surname

    def set_surname(self, other):
        try:
            if type(other) != str:
                raise PersonError("Person surname must be a string", other)
            else:
                self.__surname = other
        except PersonError as pe:
            pe.print_obj()

    def get_age(self):
        return self.__age

    def set_age(self, value):
        try:
            if value < 0:
                raise PersonError("Person age cant be a negative number:", value)
            elif type(value) != int:
                raise  PersonError("Person age must be a ineger:", value)
            else:
                self.__age = value
        except PersonError as pe:
            pe.print_obj()

    def get_gender(self):
        return self.__gender

    def set_gender(self, other):
        try:
            if type(other) != str:
                raise PersonError("Person gender must be Male or Female:", other)
            else:
                self.__gender = other
        except PersonError as pe:
            pe.print_obj()
