
import math

def distance(x1, y1, x2, y2):
    return math.sqrt(math.pow((x1-x2),2) + math.pow((y1-y2),2))

dataset = [(3, 104), (2, 100), (1,81), (101,10), (99,5), (98, 2)]
labelset = list('R'*3 + 'A'*3)

if __name__ == '__main__':
    print distance(3,104,18,90)
    for x, y in enumerate(dataset):
        print x, y

    print labelset
    print range(6)