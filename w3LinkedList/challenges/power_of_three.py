# Write a Python program to check if a given positive integer is a power of three

def is_power_three(num: int) -> bool:
    if num == 0:
        return False
    if num == 1:
        return True

    return (num % 3 == 0 and is_power_three(num/3))

if __name__ =="__main__":
    n1 = 4
    n2 = 16
    n3 = 3
    n4 = 2
    n5 = 9
    n6 = 1
    n7 = 15


    print(is_power_three(n1))
    print(is_power_three(n2))
    print(is_power_three(n3))
    print(is_power_three(n4))
    print(is_power_three(n5))
    print(is_power_three(n6))
    print(is_power_three(n7))