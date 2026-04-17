def binary_serach(a, b):
    start = 0
    end = len(a) - 1

    while start <= end:
        mid = (start + end) // 2
        if a[mid] == b:
            return mid
        elif a[mid] < b:
            start = mid + 1
        else:
            end = mid - 1
    return -1


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_serach(my_list, 5))
