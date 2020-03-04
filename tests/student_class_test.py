from student_class import Student


def test_init_repr_student(name, surname, age, gender, university, faculty, course, middle_score):
    obj = Student(name, surname, age, gender, university, faculty, course, middle_score)
    print(obj)


def test_get_university(name, surname, age, gender, university, faculty, course, middle_score):
    obj = Student(name, surname, age, gender, university, faculty, course, middle_score)
    print(obj.get_university())


def test_set_university(name, surname, age, gender, university, faculty, course, middle_score, setuniversity):
    obj = Student(name, surname, age, gender, university, faculty, course, middle_score)
    obj.set_university(setuniversity)
    print(obj)


def test_get_faculty(name, surname, age, gender, university, faculty, course, middle_score):
    obj = Student(name, surname, age, gender, university, faculty, course, middle_score)
    print(obj.get_faculty())


def test_set_faculty(name, surname, age, gender, university, faculty, course, middle_score, setfaculty):
    obj = Student(name, surname, age, gender, university, faculty, course, middle_score)
    obj.set_faculty(setfaculty)
    print(obj)


def test_get_course(name, surname, age, gender, university, faculty, course, middle_score):
    obj = Student(name, surname, age, gender, university, faculty, course, middle_score)
    print(obj.get_course())


def test_set_course(name, surname, age, gender, university, faculty, course, middle_score, setcourse):
    obj = Student(name, surname, age, gender, university, faculty, course, middle_score)
    obj.set_course(setcourse)
    print(obj)


def test_get_middle_score(name, surname, age, gender, university, faculty, course, middle_score):
    obj = Student(name, surname, age, gender, university, faculty, course, middle_score)
    print(obj.get_middle_score())


def test_set_middle_score(name, surname, age, gender, university, faculty, course, middle_score, setmiddlescore):
    obj = Student(name, surname, age, gender, university, faculty, course, middle_score)
    obj.set_middle_score(setmiddlescore)
    print(obj)
