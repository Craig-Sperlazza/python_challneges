import timeit

#two functions: Least Common Multiple and Greatest Common Factor

def least_comm_mult(num1, num2):   
    if num1 == 0 or num2 == 0:
        return "The LCM of Zero does not exist"
    elif num1 < 0 or num2 < 0:
        print("The LCM of the absolute value of all the numbers, ignoring the negative signs is:")
        num1 = abs(num1)
        num2 = abs(num2)
    temp = [num1, num2]
    greatest = max(temp)
    smallest = min(temp)

    for i in range(1, greatest + 1):
        possible_num = greatest * i
        if possible_num % smallest == 0:
            return f"The LCM is: {possible_num}"


def great_comm_fact(num1, num2): 
    if num1 < 0 or num2 < 0:
        return ("Do not use negative values. The GCF is only defined for positive numbers (integers).")
    elif num1 == 0:
        return(f"The GCF is {num2}")
    elif num2 == 0:
        return(f"The GCF is {num1}")
    else:
        factor_list = []
        temp = [num1, num2]
        smaller_num = min(temp)
        # if num1 > num2:
        #     smaller_num = num2
        # else: 
        #     smaller_num = num1
        for i in range(1, smaller_num + 1):
            if num1 % i == 0 and num2 % i == 0:
                factor_list.append(i)
        gcf = max(factor_list)

        return(f"The common factors of {num1} and {num2} are: {factor_list} \nThe GCF is {gcf}")

#multiple numbers
def findgcd(num1, num2):
    while(num2):
        # num1, num2 = num2, num1 % num2
        temp = num1
        num1 = num2
        num2 = temp % num2
        # print(num2)
    return num1

l = [22, 44, 66, 88, 99]
num1=l[0]
num2=l[1]
gcd=findgcd(num1,num2)
for i in range(2,len(l)):
   gcd=findgcd(gcd,l[i])
print(f"gcd is: {gcd}")


print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

if __name__ == '__main__':
    # print(least_comm_mult(15, 35))
    # print(least_comm_mult(0, 35))
    # print(least_comm_mult(30, 36))
    # print(least_comm_mult(30, -36))
    # print(least_comm_mult(4, 3))
    # print(least_comm_mult(123453235, 133322234))

    print(great_comm_fact(15, 35))
    print(great_comm_fact(12, 8))
    print(great_comm_fact(50, 280))
    print(great_comm_fact(0, 35))
    print(great_comm_fact(30, -36))


