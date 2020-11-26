# https://leetcode.com/problems/two-sum/

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

from typing import List, Optional 

def twoSum(nums: List[int], target: int) -> List[int]:
    ans = []
    for index1, value1 in enumerate(nums):
        for index2, value2 in enumerate(nums):
            if len(ans) > 0:
                return ans
            elif value1 + value2 == target and index2 != index1:
                ans.append(index1)
                ans.append(index2)
                
    return ans

if __name__== "__main__":
    test = [1, 2, 3, 4]
    val = 7

    print(twoSum(test, val))