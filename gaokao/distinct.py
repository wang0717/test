#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：test 
@File    ：distinct.py
@Author  ：Wang
@Date    ：2022/5/19 0:18 
@Show    :
"""
def distinct2(l): #运行时间太长
    lst = list(l)
    num = []
    tmp = []

    for it in lst:
        if it[0] not in num:
            num.append(it[0])
            tmp.append(it)
        elif it[0] in num:
            del it
    return tmp

def distinct(l):
    lst = list(l)
    num = len(lst)
    i = 0
    while i<num-1 :
        if lst[i][0] == lst[i + 1][0]:
            del lst[i + 1]
            num = num - 1
            i=i+1
        else:
            i=i+1
    # for i in range(0,num):
    #     if lst[i][0] == lst[i+1][0]:
    #         del lst[i+1]
    #         num = num-1
    return lst


