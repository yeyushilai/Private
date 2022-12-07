# -*- coding:utf-8 -*-


class Person(dict):
    def __init__(self, name, age, *args, **kwargs):
        super(Person, self).__init__(*args, **kwargs)
        self.name = name
        self.age = age


    def __setitem__(self, key, value, *args, **kwargs):
        """对字典对象的键值对赋值，本质上是调用__setitem__方法"""
        print("exec __setitem__, key: %s, value: %s" % (key, value))
        setattr(self, key, value)

    def __getitem__(self, key, *args, **kwargs):
        """获取字典对象的key对应的值时，本质上是调用对象的___getitem__"""
        print("exec __getitem__, key: %s" % key)
        return getattr(self, key)




if __name__ == '__main__':
    person = Person(name="john", age=33)
    person["name"] = "zhangsan"
    # exec __setitem__, key: name, value: zhangsan
    a = person["name"]
    # exec __getitem__, key: name
