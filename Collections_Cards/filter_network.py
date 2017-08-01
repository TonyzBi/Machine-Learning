#!/usr/bin/env python
# -*- encoding: utf-8 -*-

net_dic = {}
def main():
    with open('network.txt', 'r') as net_file:
        global net_dic
        vlanName = ''
        segmentId = ''
        for line in net_file.readlines():
            if 'name' in line:
                vlanName = line[30:67].strip()
            if 'provider:segmentation_id' in line:
                segmentId = line[30:67].strip()
                net_dic[vlanName] = segmentId

    for item in net_dic.keys():
        print '%s' % item, ' '*(20-len(item)),': %s' % net_dic[item]

if __name__ == '__main__':
    main()