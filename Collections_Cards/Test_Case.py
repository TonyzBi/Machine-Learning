s1 = 'hello world, %s'
print s1 % 'hai'

s2 = "this is a test string".replace('is','new', 1)
print s2

s3 = "*******replace: EpsIndDefContextId :::::".strip('*:')
print s3

items = [('name','Gumby'),('age',42)]
dic1 = dict(items)
print dic1

dic2 = dict(name='Gumby', age=42)
print dic2

phonebook = {'Alice':'2341','Cecil':'3258'}

print "Cecil 's phone number is %(Cecil)s " % phonebook

dic3 = {'name':'Robin','girlfriend':'Marin'}

key, value = dic3.popitem()
print key, value

print '###################################'

for key, value in phonebook.items():
    print key, value

for key in phonebook:
    print key
#age = 10
#assert 0 < age < 100, 'The age must be realistc'

names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]
l1 = zip(names, ages)
print l1
print dict(l1)

for index, name in enumerate(names):
    print index, name

from math import sqrt
for n in range(99, 81, -1):
    root = sqrt(n)
    if root == int(root):
        print n
        break
else:
    print "Didn't find it!"

fibs = [0 ,1]
for i in range(8):
    fibs.append(fibs[-2] + fibs[-1])

print fibs

def hello(name):
    print 'hello , ' + name

hello('python')

def fibs_fun(num):
    result = [0 ,1]
    for i in range(num-2):
        result.append(result[-2] + result[-1])

    return result

print fibs_fun(10)

def print_params(*params):
    print params

print_params('Testing', 'programer')

def dic_params(**params):
    print params

dic_params(x = 1, y = 2, c = 'nn')


def pow(x, y):
    if y == 0:
        return 1
    else:
        return x * pow(x, y - 1)

print pow(2, 7)

def bsearch(sequence, number, lower, upper):
    if upper is None:
        upper = len(sequence) - 1
    if lower == upper:
        return lower
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return bsearch(sequence, number, middle + 1, upper)
        else:
            return bsearch(sequence, number, lower, middle)



s1 = [1, 2, 5, 9, 10, 23, 26, 38, 90]
print bsearch(s1, 23, 0, None)

def larger(x):
    if x  > 10:
        return True
    else:
        return False

print filter(larger, s1)

print 'abc'.ljust(20),'end'

from fractions import Fraction

print Fraction(18, 10) + Fraction(1, 5)

class Person():
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def greet(self):
        print "Hello, %s" % self.name

Bob = Person()
Bob.setName("Bob Li")
Bob.greet()

class Rect:
    def __init__(self):
        self.width = 0
        self.height = 0
    def setSize(self, size):
        self.width, self.height = size
    def getSize(self):
        return self.width, self.height
    size = property(getSize, setSize)



r = Rect()
r.width = 5
r.height = 10
print r.size

r.size = 150, 100
print r.size
print r.height


def SelectedSort(inList):
    minIndex = 0
    for i in range(len(inList)):
        minIndex = i
        for j in range(i+1, len(inList)):
            if inList[j] < inList[minIndex]:
                minIndex = j

        if minIndex != i:
            temp = inList[minIndex]
            del inList[minIndex]
            inList.insert(i, temp)

    return inList

sList = [1, 9, 8, 20, 16, 3, 7, 4]
print SelectedSort(sList)


# wait to wait until you enter a word
# word = ''
# while not word:
#    word = raw_input("Please enter a word: ")

print 190*60
print 'Page 178'

