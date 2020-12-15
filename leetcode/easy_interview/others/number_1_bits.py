# Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

def hammingWeight(n: int) -> int:
    c = 0
    while n:
        # this will take out the right-most 1 of n
        n = n & (n - 1)
        c += 1
    return c



if __name__=="__main__":
    n = 100000000000000000000000000001011
    print(hammingWeight(n))
    #output 4

    n2 = 100000000000000000000000010000000
    print(hammingWeight(n2))
    #output 2