# -*- coding:utf-8 -*-

from weakref import WeakKeyDictionary


class Grade(object):
    def __init__(self):
        self._values = WeakKeyDictionary()

    def __get__(self, instance, instance_type):
        if instance is None:
            return None
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not ( 0<=value<=100):
            raise ValueError("Grade must be in 0 .. 100")
        self._values[instance] = value


class Student(object):
    cn = Grade()
    en = Grade()


p1 = Student()
p1.cn = 90
p1.en = 101
