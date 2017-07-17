# -*- coding: utf-8 -*-


def outer(fun):
    def Wrapper(arg):
        print 'Wrapper: 毕海'
        result = fun(arg)
        return result

    return Wrapper

@outer
def fun1(arg):
    return arg + 1

print fun1(1)

