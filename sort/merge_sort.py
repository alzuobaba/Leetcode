# Python program for implementation of RergeSort

import copy

def merge_sort(arr, lo, hi):
# 自上而下的方式
    if lo >= hi:
        return
    mid = lo + (hi-lo)//2
    merge_sort(arr, lo, mid)
    merge_sort(arr, mid+1, hi)
    merge(arr, lo, mid, hi)

def merge(arr, lo, mid, hi):
    arr_copy = copy.deepcopy(arr)
    i = k=lo 
    j = mid + 1
    while k <= hi:
        if i > mid:
            arr[k] = arr_copy[j]
            j += 1
        elif j > hi:
            arr[k] = arr_copy[i]
            i += 1
        elif arr_copy[i] > arr_copy[j]:
            arr[k] = arr_copy[j]
            j +=1
        else:
            arr[k] = arr_copy[i]
            i +=1
        k+=1


# Driver program
if __name__ == '__main__':
    arr = [6, 5, 12, 10, 9, 1]
    merge_sort(arr, 0, len(arr)-1)
    print(arr)
