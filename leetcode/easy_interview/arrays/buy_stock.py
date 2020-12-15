from typing import List

def maxProfit(nums: List[int]) -> bool:
    profit = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            profit += (nums[i] - nums[i-1])
    return profit

    



if __name__ == "__main__":
    x = [7,1,5,3,6,4]
    print(maxProfit(x))

    y = [1,2,3,4,5]
    print(maxProfit(y))

    z = [7,6,4,3,1]
    print(maxProfit(z))
