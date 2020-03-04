from teacher_class import Teacher
from money_class import Money


def test_init_repr_teacher(name, surname, age, gender, university, faculty, discipline, experience, amount, currency):
    m = Money(amount, currency)
    obj = Teacher(name, surname, age, gender, university, faculty, discipline, experience, m)
    print(obj)

#test_init_repr_teacher("Martin", 'Vardanyan', 23, 'Male', "RAU", "Economic", "MArketing", 5, 700, 'rub')


def test_set_university(name, surname, age, gender, university, faculty, discipline, experience, amount, currency, set_university):
    m = Money(amount, currency)
    obj = Teacher(name, surname, age, gender, university, faculty, discipline, experience, m)
    obj.set_university(set_university)
    print(obj)


def test_set_faculty(name, surname, age, gender, university, faculty, discipline, experience, amount, currency, set_faculty):
    m = Money(amount, currency)
    obj = Teacher(name, surname, age, gender, university, faculty, discipline, experience, m)
    obj.set_faculty(set_faculty)
    print(obj)


def test_set_discipline(name, surname, age, gender, university, faculty, discipline, experience, amount, currency, set_discipline):
    m = Money(amount, currency)
    obj = Teacher(name, surname, age, gender, university, faculty, discipline, experience, m)
    obj.set_discipline(set_discipline)
    print(obj)


def test_set_experience(name, surname, age, gender, university, faculty, discipline, experience, amount, currency, set_experience):
    m = Money(amount, currency)
    obj = Teacher(name, surname, age, gender, university, faculty, discipline, experience, m)
    obj.set_experience(set_experience)
    print(obj)


def test_set_salary(name, surname, age, gender, university, faculty, discipline, experience, amount, currency, amount2, currency2):
    m = Money(amount, currency)
    obj = Teacher(name, surname, age, gender, university, faculty, discipline, experience, m)
    m1 = Money(amount2, currency2)
    obj.set_salary(m1)
    print(obj)

#test_set_salary("Martin", 'Vardanyan', 23, 'Male', "RAU", "Economic", "MArketing", 5, 700, 'rub', 1000, 'usd')

def test_set_currency(name, surname, age, gender, university, faculty, discipline, experience, amount, currency, set_currency):
    m = Money(amount, currency)
    obj = Teacher(name, surname, age, gender, university, faculty, discipline, experience, m)
    obj.set_currency(set_currency)
    print(obj)


def test_get_university(name, surname, age, gender, university, faculty, discipline, experience, amount, currency):
    m = Money(amount, currency)
    obj = Teacher(name, surname, age, gender, university, faculty, discipline, experience, m)
    print(obj.get_university())


def test_get_faculty(name, surname, age, gender, university, faculty, discipline, experience, amount, currency):
    m = Money(amount, currency)
    obj = Teacher(name, surname, age, gender, university, faculty, discipline, experience, m)
    print(obj.get_faculty())


def test_get_experience(name, surname, age, gender, university, faculty, discipline, experience, amount, currency):
    m = Money(amount, currency)
    obj = Teacher(name, surname, age, gender, university, faculty, discipline, experience, m)
    print(obj.get_experience())


def test_get_discipline(name, surname, age, gender, university, faculty, discipline, experience, amount, currency):
    m = Money(amount, currency)
    obj = Teacher(name, surname, age, gender, university, faculty, discipline, experience, m)
    print(obj.get_discipline())


def test_get_salary(name, surname, age, gender, university, faculty, discipline, experience, amount, currency):
    m = Money(amount, currency)
    obj = Teacher(name, surname, age, gender, university, faculty, discipline, experience, m)
    print(obj.get_salary())


def test_get_currency(name, surname, age, gender, university, faculty, discipline, experience, amount, currency):
    m = Money(amount, currency)
    obj = Teacher(name, surname, age, gender, university, faculty, discipline, experience, m)
    print(obj.get_currency())
