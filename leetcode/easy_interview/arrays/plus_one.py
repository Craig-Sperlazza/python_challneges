# Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
# Example:
#     Input: digits = [1,2,3]
#     Output: [1,2,4]
#     Explanation: The array represents the integer 123.

from typing import List, Optional


def plusOne(digits: List[int]) -> List[int]:
    #single digit or last digit that != 9 
    if (len(digits) == 1 and digits[0] != 9) or digits[-1] != 9 :
        curr = digits[-1]
        curr += 1
        digits[-1] = curr
        return digits
    #Made a special case to deal with [9]
    elif (len(digits) == 1 and digits[0] == 9):
        return [1,0]
    
    else:
        #loop through the digits beginning in the back and when it hits a digit that !=9, increments +1 and returns
        for i in range(len(digits) - 1 , 0, -1):
            if digits[i] != 9:
                curr = digits[i]
                curr += 1
                digits[i] = curr
                return digits
            #if the current digit is 9 we have to make it a 0 and continue the loop unless 2 special cases
            #first case: if the loop increments all the way to beginning (99, 999, etc.), we have to increment i-1 to 0 and then insert a 1 at begin of list
            #second case: if the loop increments all the way to beginning but it isnt a 9(899, 7999, etc.): 
            #   we have to increment i-1 by 1 
            else:
                digits[i] = 0
                if i == 1 and digits[i-1] == 9:
                    digits[i-1] = 0
                    digits.insert(0,1)
                    return digits
                elif i == 1 and digits[i-1] != 9:
                    curr = digits[i-1]
                    curr += 1
                    digits[i-1] = curr
                    return digits


if __name__ == "__main__":
    nums = [1, 2, 3, 3, 4, 5, 5]
    print(plusOne(nums))

    nums2 = [1, 2, 3, 3, 4, 5, 9]
    print(plusOne(nums2))

    nums3 = [3]
    print(plusOne(nums3))

    nums4 = [9]
    print(plusOne(nums4))

    nums5 = [9, 9]
    print(plusOne(nums5))

    nums6 = [9, 9, 9, 9]
    print(plusOne(nums6))
    