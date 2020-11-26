# Write a function that reverses a string. The input string is given as an array of characters char[].

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

from typing import List, Optional


def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    s.reverse()
    return s




if __name__ == "__main__":
    str2 = ["h", "e", "l"]
    print(reverseString(str2))