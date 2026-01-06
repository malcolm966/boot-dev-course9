def find_max(nums):
    if nums:
        max_num = -float('inf')
        for n in nums:
            if n > max_num:
                max_num = n
        return max_num
    return None
