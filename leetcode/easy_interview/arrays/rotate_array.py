# Given an array, rotate the array to the right by k steps, where k is non-negative.

from typing import List, Optional



def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    if len(nums) == 1:
        return nums

    for _ in range(k):
        nums.insert(0, nums[len(nums)-1])
        nums.pop(-1)
    return nums

#faster solution
def rotate2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] +  nums[:-k]

if __name__ == "__main__":
    nums1 = [1, 2, 3, 3, 4, 5, 5]
    print(rotate(nums1, 3))

    
    