def subset_sum(nums:list, target:int)->bool:
    return find_subset_sum(nums, target, len(nums) - 1)


def find_subset_sum(nums, target, index) ->bool:
    if target == 0:
        return True
    if index < 0:
        return False
    if nums[index] > target:
        return find_subset_sum(nums, target, index - 1)
    else:
        result1 =  find_subset_sum(nums, target, index - 1)
        result2 = find_subset_sum(nums, target - nums[index], index - 1)
        if result1 or result2:
            return True
        else:
            return False
