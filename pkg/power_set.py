# def power_set(nums: list[int]) -> list[list[int]]:
#     res = []

#     def backtrack(index: int, path: list[int]):
#         if index == len(nums):
#             res.append(path.copy())
#             return

#         # 不选 nums[index]
#         backtrack(index + 1, path)

#         # 选 nums[index]
#         path.append(nums[index])
#         backtrack(index + 1, path)
#         path.pop()  # 回溯

#     backtrack(0, [])
#     return res

def power_set(input:list):
    if len(input) == 0:
        return [[]]
    all_subsets = list()
    all_subsets.append([])
    for i in range(len(input)):
        new_subsets = list()
        for subset in all_subsets:
            new_subset = subset.copy()
            new_subset.append(input[i])
            new_subsets.append(new_subset)
        all_subsets.extend(new_subsets)
    return all_subsets
    
run_cases = [
    ([1, 2], [[], [1], [2], [1, 2]]),
    ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
]

submit_cases = run_cases + [
    ([], [[]]),
    ([1], [[], [1]]),
    (
        [1, 2, 3, 4],
        [
            [],
            [1],
            [2],
            [1, 2],
            [3],
            [1, 3],
            [2, 3],
            [1, 2, 3],
            [4],
            [1, 4],
            [2, 4],
            [1, 2, 4],
            [3, 4],
            [1, 3, 4],
            [2, 3, 4],
            [1, 2, 3, 4],
        ],
    ),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    for i in input1:
        print(f" * {i}")
    print(f"Expected: {expected_output}")
    result = power_set(input1)
    print(f"Actual:   {result}")
    sorted_result = sorted([sorted(inner) for inner in result])
    sorted_expected_output = sorted([sorted(inner) for inner in expected_output])
    if sorted_result == sorted_expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()