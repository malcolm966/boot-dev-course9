def binary_search(target, arr:list):
    sorted_arr = list(sorted(arr))
    l = 0
    r = len(sorted_arr) - 1
    while l <= r:
        middle = (r + l) // 2
        if target > sorted_arr[middle]:
            l = middle + 1
        elif target < sorted_arr[middle]:
            r = middle - 1
        else:
            return True
    return False
