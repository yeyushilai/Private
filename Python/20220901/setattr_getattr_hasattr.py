# -*- coding:utf-8 -*-


class Person():
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    person = Person(name="yangzhuang")

    # hasattr
    if hasattr(person, "name"):
        print("attr name exists")
        # attr name exists

    # setattr
    if not hasattr(person, "age"):
        print("attr age not exists")
        # attr age not exists
    setattr(person, "age", 33)
    if not hasattr(person, "age"):
        print("attr age not exists")
    else:
        print("attr age exists")
        # attr age exists

    # getattr
    age = getattr(person, "age")
    print(age)
