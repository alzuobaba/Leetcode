#!/usr/bin/python
# -*- coding: UTF-8 -*-
array = [-2, -3, -6, 45, 0, 4, 9]


def select_sort(array):
    for i in range(1, len(array)):
        index = i-1
        for j in range(i, len(array)-1):
            if array[j] > array[index]:
                index = j
        array[i-1], array[index] = array[index], array[i-1]
    return array


def select_sort_2(array):
    for j in range(len(array)-1):
        index = j
        minest = array[index]
        for i in range(1+j, len(array)-1):
            if minest > array[i]:
                minest = array[i]
                index = i
        array[j], array[index] = array[index], array[j]

    return array





result = select_sort(array)
print(result)

