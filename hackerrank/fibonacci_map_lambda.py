# Let's learn some new Python concepts! You have to generate a list of the first  fibonacci numbers,  0 being the first number. 
# Then, apply the map function and a lambda expression to cube each fibonacci number and print the list.



def fibonacci(n):
    empty_lst = []
    single_lst = [0]
    fib_lst = [0, 1]
    a = 0
    b = 1
    i = 0

    if n == 0:
        return empty_lst
    elif n == 1:
        return single_lst
    elif n == 2:
        return fib_lst
    else:
        while i < n - 1:
            new = b + a
            a = b
            b = new
            i += 1
            fib_lst.append(new)
    return fib_lst


print("Please input a number of fibonacci items:")
int_input = int(input())   

new_list = fibonacci(int_input)

cube = list(map(lambda x: x ** 3, new_list))

# print(fibonacci(1))
# print(fibonacci(2))
# print(fibonacci(3))
print(fibonacci(int_input))
print(cube)
