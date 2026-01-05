def average_followers(nums):
    if nums:
        total = 0
        for n in nums:
            total += n
        return total / len(nums)
    return None
