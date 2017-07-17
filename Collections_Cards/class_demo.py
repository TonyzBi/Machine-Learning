# -*- coding: utf-8 -*-

class Province(object):

    #静态字段
    mem = 'Province static varibles'

    def __init__(self, name, capital):
        #动态字段
        self.__Name = name
        self.__Capital = capital

    def sport_meeting(self):
        #动态方法
        print self.__Name, " 开运动会。。。。"

    #静态方法
    @staticmethod
    def Foo():
        print "省里要反腐"

    @property
    def Capital(self):
        return self.__Capital

    @Capital.setter
    def Capital(self, cap):
        self.__Capital = cap

hlj = Province('Heilongjiang', 'Harbin')

#print hlj.Name
hlj.sport_meeting()

print Province.mem
Province.Foo()

print hlj.Capital

hlj.Capital = 'hrb'

print hlj.Capital

#print Province.Capital

class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value, int):
            raise ValueError("Error value")
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    def __call__(self):
        print "excute call method...."


s = Student()
s.score = 99

print s.score

s()


