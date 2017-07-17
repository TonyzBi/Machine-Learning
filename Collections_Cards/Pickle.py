import pickle
import json

li = [1, 3, 4, 2, 9, 10]

data = pickle.dumps(li)

print pickle.loads(data)

with open('data.pk', 'wb') as fd:
    pickle.dump(li, fd)

with open('data.pk', 'rb') as fl:
    xdata = pickle.load(fl)

print xdata

jsontext = {'a': 65, 'b': 66, 'c': 67}

jsondata = json.dumps(jsontext)

print jsondata

print json.loads(jsondata)
print '################################################'

with open('data.json', 'wb') as fd:
    json.dump(jsontext, fd, encoding='utf-8')


with open('data.json', 'rb') as fl:
    jsonloaddata = json.load(fl, encoding='utf-8')

print jsonloaddata
