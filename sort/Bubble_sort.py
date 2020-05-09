#!/usr/bin/python
# -*- coding: UTF-8 -*-
array = [-2, -3, -6, 45, 0, 4, 9]


def bubble_sort(array):
    for i in range(1, len(array)):
        for j in range(len(array)-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array



result = bubble_sort(array)
print(result)













# def bubble_sort(array):
#     greatest = array[0]
#     for j in range(len(array)-1):
#         for i in range(len(array)-j-1):
#             if array[i] > array[i+1]:
#                 array[i], array[i+1] = array[i+1], array[i]
#     return array

# def bubble_sort(array):
#     for i in range(len(array)-1):
#         for j in range(len(array)-1-i):
#             if array[j] < array[j+1]:
#                 array[j], array[j+1] = array[j+1], array[j]
#     return array