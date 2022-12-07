# -*- coding:utf-8 -*-


class Person(object):
    def __init__(self, name, age, *args, **kwargs):
        super(Person, self).__init__(*args, **kwargs)
        self.name = name
        self.age = age

    def __getattr__(self, key, *args, **kwargs):
        """当获取的属性不存在的时候，调用__getattribute__方法之后会继续调用__getattr__方法"""
        print("exec __getattr__, key: %s" % key)
        super(Person, self).__getattr__(key, *args, **kwargs)

    def __setattr__(self, key, value, *args, **kwargs):
        """实例对象设置属性时，本质上是调用了__setattr__方法"""
        print("exec __setattr__, key: %s, value: %s" % (key, value))
        super(Person, self).__setattr__(key, value, *args, **kwargs)

    def __getattribute__(self, key, *args, **kwargs):
        """实例对象获取属性时，本质上是调用__getattribute__方法
        当获取的属性不存在的时候，会继续调用__getattr__方法
        """
        print("exec __getattribute__, key: %s" % key)
        return super(Person, self).__getattribute__(key, *args, **kwargs)


if __name__ == '__main__':
    person = Person(name="john", age=33)
    name = person.name
    age = person.age
    error_attr = person.error_attr
