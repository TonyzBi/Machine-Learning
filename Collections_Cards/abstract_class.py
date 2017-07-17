from abc import ABCMeta, abstractmethod

class Interface(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def login(self):pass

class ImpleClass(Interface):
    def __init__(self):
        pass

    def login(self):
        print 'login successfully..'

try:
    Im = ImpleClass()
    Im.login()
except IOError,e:
    print e
else:
    print 'No error'
finally:
    print 'wrap up'


class MyError(Exception):
    def __init__(self, msg):
        self.__msg = msg
    def __str__(self):
        return self.__msg


