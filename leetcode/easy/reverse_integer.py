# Given a 32-bit signed integer, reverse digits of an integer.

# Note:
# Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

# -2147483648
# 2147483647

from typing import Optional, List

def reverse(x: int) -> int:
    xstr = str(x)
    if len(xstr) == 1:
        return int(xstr)
    elif len(xstr) == 2 and xstr[0] == "-":
        return int(xstr)
    elif xstr[0] == "-":
        xstr_positive = xstr[1:]
        rev_xstr = xstr_positive[::-1]
        rev_xstr_negative = "-" + rev_xstr
        rev_xint = int(rev_xstr_negative)

        #must check for signed 32-bit int overflow after reversed
        if rev_xint < -2147483648 or rev_xint > 2147483647:
            return 0
        return rev_xint
    else:
        rev_xstr = xstr[::-1]
        rev_xint = int(rev_xstr)
        if rev_xint < -2147483648 or rev_xint > 2147483647:
            return 0
        return rev_xint



if __name__ == "__main__":
    print("-----Testing Single Digits---if-----")
    test = 2
    test1 = 0
    print(reverse(test))
    print(reverse(test1))

    print("-----Testing Single Negative Digits---elif1-----")
    test2 = -1
    print(reverse(test2))

    print("-----Testing Multi Negative Digits---elif2-----")
    test3 = -46743
    test4 = -230
    test5 = -3030000000000
    print(reverse(test3))
    print(reverse(test4))
    print(reverse(test5))

    print("-----Testing Multi Digits---else-----")
    test6 = 46743
    test7 = 230
    test8 = 30000000000
    print(reverse(test6))
    print(reverse(test7))
    print(reverse(test8))

    print("-----Actual leet code tests-------")
    leet1 = 1534236469
    too_b = 2147483647
    print(reverse(leet1))