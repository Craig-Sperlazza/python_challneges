# Given a 32-bit signed integer, reverse digits of an integer.

# Note:
# Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

def reverse(x: int) -> int:
    x_string = str(x)

    #if negative
    if x_string[0] == '-':
        x_string_slice = x_string[1:]
        x_rev = x_string_slice[::-1]
        x_rev = "-" + x_rev
    else:
        x_rev = x_string[::-1]
    
    x_rev_int = int(x_rev)

    #account for size
    if x_rev_int < -2147483648 or x_rev_int > 2147483647:
        return 0
    return x_rev_int

if __name__ == "__main__":
    x = 123
    print(reverse(x))

    y = -123
    print(reverse(y))

    z = 120
    print(reverse(z))

    a = 0
    print(reverse(a))
