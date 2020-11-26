# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

from typing import List, Optional

# #recursive
# def isPalindrome(s: str) -> bool:
#     #get rid of spaces, special characters, and make it all lowercase
#     s2 = ''.join(e for e in s if e.isalnum())
#     s3 = s2.lower()
    
#     if not s3:
#         return True
#     elif len(s3) == 1:
#         return True
#     else:
#         if s3[0] != s3[-1]:
#             return False
#         return isPalindrome(s3[1:-1])
    
#iterative
def isPalindrome(s: str) -> bool:
    #get rid of spaces, special characters, and make it all lowercase
    s3 = ''.join(e for e in s if e.isalnum()).lower()

    for _ in range(len(s3)//2):
        if not s3:
            return True
        elif len(s3) == 1:
            return True
        elif len(s3) == 2 and s3[0] != s3[-1]:
            return False
        else:
            if s3[0] != s3[-1]:
                return False
            s3 = s3[1:-1]
            
    return True

if __name__ == "__main__":
    str1 = "A man, a plan, a canal: Panama"
    print(isPalindrome(str1))

    str2 = "race a car"
    print(isPalindrome(str2))

    str3 = ""
    print(isPalindrome(str3))

    str4 = "a"
    print(isPalindrome(str4))

    str5 = "aa"
    print(isPalindrome(str5))

    str6 = "aa"
    print(isPalindrome(str6))

    str7 = "aba"
    print(isPalindrome(str7))

    str8 = "abba"
    print(isPalindrome(str8))

    str9 = "abb"
    print(isPalindrome(str9))

    