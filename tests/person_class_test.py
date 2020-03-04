from person_class import Person


def test_init_repr(name, surname, age, gender):
    obj = Person(name, surname, age, gender)
    print(obj)


def test_get_name(name, surname, age, gender):
    obj = Person(name, surname, age, gender)
    print(obj.get_name())


def test_set_name(name, surname, age, gender, setname):
    obj = Person(name, surname, age, gender)
    obj.set_name(setname)
    print(obj)


def test_get_surname(name, surname, age, gender):
    obj = Person(name, surname, age, gender)
    print(obj.get_surname())


def test_set_surname(name, surname, age, gender, setsurname):
    obj = Person(name, surname, age, gender)
    obj.set_surname(setsurname)
    print(obj)


def test_get_age(name, surname, age, gender):
    obj = Person(name, surname, age, gender)
    print(obj.get_age())


def test_get_gender(name, surname, age, gender):
    obj = Person(name, surname, age, gender)
    print(obj.get_gender())


def test_set_gender(name, surname, age, gender, setgender):
    obj = Person(name, surname, age, gender)
    obj.set_gender(setgender)
    print(obj)


def test_set_age(name, surname, age, gender, setage):
    obj = Person(name, surname, age, gender)
    obj.set_age(setage)
    print(obj)
