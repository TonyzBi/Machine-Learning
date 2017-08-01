# -*- coding: utf-8 -*-


class indexMap(object):
    """
    It will store the index of data and the list of data, for example:
    86159 ['8615963507702\n', '8615963556321\n', '8615953587694\n', '8615965164189\n', '8615949897579\n', '8615953513713\n']
    86158 ['8615863845259\n', '8615866120152\n', '8615853572716\n']
    """
    def __init__(self):
        self.mapTable = {}
        self.size = 0

    def add(self, cutlen = 0, data = None):
        """
        :param cutlen: the length of you want to cut data string
        :param data: String of data you want to store
        :return: None
        """
        if len(data) <= cutlen or data == None:
            print data, "is invalid data, please check"
            # raise IndexError('cut is not invalid!!')
        else:
            index = data[0:cutlen]

            if self.mapTable.get(index, -1) == -1:
                self.mapTable[index] = []

            self.mapTable[index].append(data)
            self.size += 1

    def __contains__(self, item):
        cut = 0

        if self.mapTable:
            cut = len(self.mapTable.keys()[0])
            if cut > len(item):
                return False
        item = str(item)
        indexs = item[0:cut]

        return item in self.mapTable.get(indexs)

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.mapTable.iteritems()

    def showStastics(self):
        print 'Indexs : Number of Data'
        for key in self.mapTable.keys():
            print key, " : " , len(self.mapTable.get(key))


if __name__ == '__main__':
    indexdata = indexMap()
    with open('C:\\local_data\\Temp\\allUsers.txt', 'r') as numFile:
        for line in numFile:
            indexdata.add(9, line.rstrip())

    # indexdata.add(3, '1381')
    # indexdata.add(3, '1382')
    # indexdata.add(3, '1383')
    # indexdata.add(3, '1384')
    #
    # indexdata.add(3, '1391')
    # indexdata.add(3, '1392')
    # indexdata.add(3, '1393')
    print len(indexdata)
    # for key, val in indexdata:
    #     print key, val
    # while True:
    #     num = raw_input('please input your num: ')
    #     if num == 0:
    #         break
    #     print num in indexdata
    #
    indexdata.showStastics()

