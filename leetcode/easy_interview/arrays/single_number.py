#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

from typing import List, Optional


def singleNumber(nums: List[int]) -> int:
    count_dict = {}
    for item in nums:
        if item in count_dict.keys():
            count_dict[item] = 2
        else:
            count_dict[item] = 1
    for key, value in count_dict.items():
        if value == 1:
            return key

# def singleNumber(self, nums: List[int]) -> int:
#         distinct = set(el for el in nums)
#         s1 = sum(distinct)
#         s2 = sum(nums)
#         return 2*s1 - s2


if __name__ == "__main__":
    test = [1,1,2,2,3,4,4,5,5]
    print(singleNumber(test))