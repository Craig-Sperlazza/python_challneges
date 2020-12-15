# Write a Python program to check if a given positive integer is a power of two

def is_power_two(num: int) -> bool:
    if num == 0:
        return False
    if num == 2 or num == 1:
        return True

    return (num % 2 == 0 and is_power_two(num / 2))

if __name__ =="__main__":
    n1 = 4
    n2 = 16
    n3 = 11
    n4 = 64
    n5 = 10
    n6 = 1

    print(is_power_two(n1))
    print(is_power_two(n2))
    print(is_power_two(n3))
    print(is_power_two(n4))
    print(is_power_two(n5))
    print(is_power_two(n6))