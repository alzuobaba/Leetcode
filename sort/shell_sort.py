def shell_sort(arr):
    a_lenth = len(arr)
    gap = a_lenth//2
    while gap >= 1:
        for index in range(gap, a_lenth):
            temp = arr[index]
            j = index
            while j-gap >= 0 and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap //= 2


arr = [9, 8, 3, 7, 5, 6, 4, 1]
shell_sort(arr)
print(arr)