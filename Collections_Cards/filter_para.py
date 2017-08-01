#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import re

net_list = []
def main():
    with open('vyos.yaml', 'r') as net_file:
        global net_list
        pattern = re.compile(r'\{get_param: \w\}',re.S)
        for line in net_file.readlines():
            net_list.extend(re.findall(pattern,line))

    print net_list
    net_file.closed()

if __name__ == '__main__':
    main()