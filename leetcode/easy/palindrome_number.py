# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

# Follow up: Could you solve it without converting the integer to a string?

from typing import Optional, List

def isPalindrome(x: int) -> bool:
    xstr = str(x)

    if xstr[0] == "-":
        return False
    
    else:
        if xstr[0] == xstr[-1]:
            xstr = xstr[1:-1]
            if len(xstr) == 1 or len(xstr) == 0:
                return True
            else:
                return isPalindrome(xstr)
        return False


if __name__ == "__main__":
    
    print(isPalindrome(0))
    print(isPalindrome(-5))
    print(isPalindrome(5))
    print(isPalindrome(101))
    print(isPalindrome(111))
    print(isPalindrome(123))
    print(isPalindrome(1000021))
