# Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

from typing import List, Optional


def removeDuplicates(nums: List[int]) -> int:
    for i in range(len(nums)-1, 0, -1):
        if nums[i] == nums[i-1]:
            del nums[i]
        
            
    return len(nums), nums

if __name__ == "__main__":
    nums = [1, 2, 3, 3, 4, 5, 5]
    print(removeDuplicates(nums))

    nums2 = [1, 1, 2]
    print(removeDuplicates(nums2))

    nums3 = [0,0,0,0,0]
    print(removeDuplicates(nums3))

    nums4 = [-3,-1,-1,0,0,0,0,0,2]
    print(removeDuplicates(nums4))