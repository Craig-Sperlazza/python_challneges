from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    set_nums = set(nums)
    if len(nums) == len(set_nums):
        return False
    return True
    



if __name__ == "__main__":
    x = [1,2,3,4]
    print(containsDuplicate(x))

    y = [1,2,3,3,4]
    print(containsDuplicate(y))

    z = [1,2,3,1]
    print(containsDuplicate(z))
