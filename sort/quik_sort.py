#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Shell sort in python


def shellSort(array):
    lenth = len(array)
    h = 1   # h 为 步长
    ## 给出一个固定序列， 这个看个人怎么给，学前辈的没错
    while h < lenth // 3 :
        h = 3*h + 1

    insert_len = lenth//3



data = [9, 8, 3, 7, 5, 6, 4, 1]
shellSort(data)
print('Sorted Array in Ascending Order:')
print(data)