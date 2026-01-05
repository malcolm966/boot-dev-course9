def find_minimum(nums):
    minimum = float('inf')
    if nums:
        for n in nums:
            if n < minimum:
                minimum = n
        return minimum
    return None
