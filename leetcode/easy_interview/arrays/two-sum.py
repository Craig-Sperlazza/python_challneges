# Given an array of integers nums and an integer target,
# return indices (in a list) of the two numbers such that they add up to target.

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    return_list = []
    for i, v in enumerate(nums):
        for j, val2 in enumerate(nums):
            if i != j:
                if v + val2 == target:
                    return_list.append(i)
                    return_list.append(j)
                    return return_list

if __name__ == "__main__":
    test1 = [1, 2, 3, 4, 5]
    targ1 = 8

    print(twoSum(test1, targ1))