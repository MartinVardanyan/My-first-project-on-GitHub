from person_class import Person


class StudentError(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_obj(self):
        print(self.a, self.b)


class Student(Person):
    def __init__(self, name: str, surname: str, age: int, gender: str, university: str, faculty: str, course: int, middle_score: int):
        super().__init__(name, surname, age, gender)
        try:
            if type(university) != str:
                raise StudentError("Student university must be a string:", university)
            elif type(faculty) != str:
                raise StudentError("Student faculty must be a string:", faculty)
            elif type(course) != int:
                raise StudentError("Student course must be a integer:", course)
            elif course <= 0:
                raise StudentError("Student course cant be a negative number:", course)
            elif type(middle_score) != int:
                raise StudentError("Student middle score must be a integer:", middle_score)
            elif middle_score < 0:
                raise StudentError("Student middle score cant be a negative number:", middle_score)
            elif middle_score > 100:
                raise StudentError("Student middle score can be more than 100:", middle_score)
            else:
                self.__university = university
                self.__faculty = faculty
                self.__course = course
                self.__middle_score = middle_score
        except StudentError as st:
            st.print_obj()

    def __repr__(self):
        return super().__repr__() + "( {}-{} - {}-Course - {}-Middle Score )".format(self.__university, self.__faculty, self.__course, self.__middle_score)

    def get_university(self):
        return self.__university

    def set_university(self, other):
        try:
            if type(other) != str:
                raise StudentError("Student university must be a string:", other)
            else:
                self.__university = other
        except StudentError as st:
            st.print_obj()

    def get_faculty(self):
        return self.__faculty

    def set_faculty(self, other):
        try:
            if type(other) != str:
                raise StudentError("Student faculty must be a string:", other)
            else:
                self.__faculty = other
        except StudentError as st:
            st.print_obj()

    def get_course(self):
        return self.__course

    def set_course(self, other):
        try:
            if type(other) != int:
                raise StudentError("Student course must be a integer:", other)
            elif other <= 0:
                raise StudentError("Student course cant be zero or negative number:", other)
            else:
                self.__course = other
        except StudentError as st:
            st.print_obj()

    def get_middle_score(self):
        return self.__middle_score

    def set_middle_score(self, other):
        try:
            if other < 0:
                raise StudentError("Student middle score cant be negative number:", other)
            elif other > 100:
                raise StudentError("Student middle score cant be more than 100:", other)
            elif type(other) != int:
                raise StudentError("Student middle score must be a integer:", other)
            else:
                self.__middle_score = other
        except StudentError as st:
            st.print_obj()
