# Given an integer n, return true if it is a power of three. Otherwise, return false.

def isPowerOfThree(n: int) -> bool:
    # if n == 0:
    #     return False
    # if n == 1:
    #     return True
    # while n % 3 == 0:
    #     n = n / 3
    # return n == 1

    if n == 0:
        return False
    if n == 1:
        return True
    return ((n % 3) == 0) and isPowerOfThree(n/3)

if __name__  == '__main__':
    n1 = 27
    n2 = 0
    n3 = 9
    n4 = 45
    n5 = 16

    print(isPowerOfThree(n1))
    print(isPowerOfThree(n2))
    print(isPowerOfThree(n3))
    print(isPowerOfThree(n4))
    print(isPowerOfThree(n5))