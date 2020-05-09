#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 前向遍历不能将值向后移动， 那就选择后向遍历


def insert_sort_1(arr):
    for step in range(1, len(arr)):
        need_insert_value = arr[step]
        j = step - 1
        while j > 0 and need_insert_value < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = need_insert_value


def insert_Sort_2(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        # Place key at after the element just smaller than it.
        array[j + 1] = key


def insert_sort_3(arr):
    l = len(arr)

    for t in range(l):
        need_swap = arr[t]
        m = t-1
        while(m > 0 and need_swap < arr[m]):
            arr[m+1] = arr[m]
            m -= 1
        arr[m+1] = need_swap



if __name__ == '__main__':
    arr = [3, 41, 12, 324, 5]
    insert_sort_3(arr)
    print(arr)


# Insertion sort in Python


