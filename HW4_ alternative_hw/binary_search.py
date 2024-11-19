def binary_search(array: list, target):
    l, r = 0, len(array) - 1
    while l <= r:
        mean = round((l+r) / 2)
        if target > array[mean]:
            l = mean+1
        elif target < array[mean]:
            r = mean-1
        else:
            return mean
    return -1