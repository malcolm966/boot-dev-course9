def tsp(cities, paths, dist):
    all = permutations(cities)
    for p in all:
        total_dist = 0
        for i in range(len(p) - 1):
            total_dist += paths[p[i]][p[i + 1]]
        if total_dist < dist:
            return True
    return False


# don't touch below this line


def permutations(arr):
    res = []
    res = helper(res, arr, len(arr))
    return res


def helper(res, arr, n):
    if n == 1:
        tmp = arr.copy()
        res.append(tmp)
    else:
        for i in range(n):
            res = helper(res, arr, n - 1)
            if n % 2 == 1:
                arr[n - 1], arr[i] = arr[i], arr[n - 1]
            else:
                arr[0], arr[n - 1] = arr[n - 1], arr[0]
    return res

def verify_tsp(paths, dist, actual_path):
    total_path = 0
    for i in range(len(actual_path) - 1):
        total_path += paths[actual_path[i]][actual_path[i + 1]]
    return total_path < dist

