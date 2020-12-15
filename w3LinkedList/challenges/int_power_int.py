# Write a Python program to check if an integer is the power of another integer

def int_power(big: int, small: int) -> bool:
    if big == 0:
        return True
    if small == 1:
        return True
    power = 0
    while ((small ** power) <= big):
        # print(small, big, power)
        # print(small ** power)
        if (small ** power) == big:
            return True
        power += 1
    return False

if __name__ =="__main__":
    n1 = 4
    x1 = 2
    x0 = 1

    n2 = 16
    x2 = 3
    x3 = 4

    n3 = 27
    x5 = 3
    x6 = 9

    print(int_power(n1, x1))
    print(int_power(n1, x0))

    print(int_power(n2, x2))
    print(int_power(n2, x3))

    print(int_power(n3, x5))
    print(int_power(n3, x6))