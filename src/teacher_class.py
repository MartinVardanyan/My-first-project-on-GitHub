from person_class import Person
from money_class import Money


class TeacherError(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_obj(self):
        print(self.a, self.b)


class Teacher(Person):
    def __init__(self, name: str, surname: str, age: int, gender: str, university: str, faculty: str, discipline: str, experience: int, salary):
        super().__init__(name, surname, age, gender)
        try:
            if type(university) != str:
                raise TeacherError("University must be a string:", university)
            elif type(faculty) != str:
                raise TeacherError("Faculty must be a string:", faculty)
            elif type(discipline) != str:
                raise TeacherError("Discipline must be a string:", discipline)
            elif type(experience) != int:
                raise TeacherError("Experience must be a integer:", experience)
            elif experience < 0:
                raise TeacherError("Experience cant be a negative number:", experience)
            elif type(salary) != Money:
                raise TeacherError("Salary must be a Money object:", salary)
            else:
                self.__university = university
                self.__faculty = faculty
                self.__discipline = discipline
                self.__experience = experience
                self.__salary = salary
        except TeacherError as te:
            te.print_obj()

    def __repr__(self):
        return super().__repr__() + " -- {}-{}-{} - Experience:{} year, Salary:{}".format(self.__university, self.__faculty, self.__discipline, self.__experience, self.__salary)

    def get_university(self):
        return self.__university

    def get_faculty(self):
        return self.__faculty

    def get_discipline(self):
        return self.__discipline

    def get_experience(self):
        return self.__experience

    def get_salary(self):
        return self.__salary

    def get_currency(self):
        return self.__currency

    def set_university(self, other):
        try:
            if type(other) != str:
                raise TeacherError('University must be a string:', other)
            else:
                self.__university = other
        except TeacherError as te:
            te.print_obj()

    def set_faculty(self, other):
        try:
            if type(other) != str:
                raise TeacherError("Faculty must be a strng:", other)
            else:
                self.__faculty = other
        except TeacherError as te:
            te.print_obj()

    def set_discipline(self, other):
        try:
            if type(other) != str:
                raise TeacherError("Discipline ,ust be a string:", other)
            else:
                self.__discipline = other
        except TeacherError as te:
            te.print_obj()

    def set_experience(self, other):
        try:
            if type(other) != int:
                raise TeacherError("Experience must be a integer:", other)
            elif other < 0:
                raise TeacherError("Experience cant be a negative number:", other)
            else:
                self.__experience = other
        except TeacherError as te:
            te.print_obj()

    def set_salary(self, other):
        try:
            if type(other) != Money:
                raise TeacherError("Salary must be a integer:", other)
            else:
                self.__salary = other
        except TeacherError as te:
            te.print_obj()

    def set_currency(self, other):
        try:
            if type(other) != str:
                raise TeacherError("Currency must be a string:", other)
            else:
                self.__currency = other
        except TeacherError as te:
            te.print_obj()

'''m = Money(600, 'usd')
print(m)
t = Teacher("Martin", 'Vardanyan', 23, 'Male', "RAU", "Economic", "Marketing", 5, m)
print(t)'''