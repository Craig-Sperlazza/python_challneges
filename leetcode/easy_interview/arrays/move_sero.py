# Given an array nums, write a function to move (in place) all 0's to the end of it
# while maintaining the relative order of the non-zero elements.

from typing import List

def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    insert_index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insert_index] = nums[i]
            insert_index += 1

    for i in range(insert_index, len(nums)):
        nums[i] = 0

    return nums

    # for i in range(len(nums)):
    #     if nums[i] == 0:
    #         nums[i] = 'x'
    #         nums.append(0)
    # print(nums)
    # nums = [i for i in nums if i != 'x']
    # print(nums)
    # return nums


if __name__ == "__main__":
    test1 = [0,1,0,3,12]
    print(moveZeroes(test1))

    test2 = [0,0,1]
    print(moveZeroes(test2))