# Count the number of prime numbers less than a non-negative number, n.

def countPrimes(n: int) -> int:
    # count = 0
    # for i in range(2, n):
    #     prime = True
    #     num = i - 1
    #     while num > 1:
    #         # print (f"i is {i}, num is {num}")
    #         if i % num == 0:
    #             prime = False
    #             break
    #         num -= 1
    #     if prime == True:
    #         count += 1
    # return count
    if n == 0 or n == 1 or n == 2:
        return 0
    elif n == 3:
        return 1
    elif n == 4 or n == 5:
        return 2
    else:
        prime = False
        count = 2
        for num in range(1, n+1):
            if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
                prime = False
            else:
                for i in range(1, n, 2):
                    if num % i == 0:
                        prime = False
                    else:
                        prime = True
            if prime == True:
                count += 1
        return count


if __name__ == "__main__":
    n = 10
    print(countPrimes(n)) #4 primes less than 10

    m = 0
    print(countPrimes(m))  # 0 primes less than 0

    x = 1
    print(countPrimes(x))  # 0 primes less than 1

    y = 3
    print(countPrimes(3))  # 1 primes less than 1