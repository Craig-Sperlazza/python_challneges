# https://www.hackerrank.com/challenges/exceptions/problem

def except_test(a, b):
    try:
        int(a)
    except ValueError as e:
        return f"Error Code: {e}"
    try:
        int(b)
    except ValueError as e:
        return f"Error Code: {e}"
    try:
        return int(a / b)
    except ZeroDivisionError as e:
        return f"Error Code: integer division or modulo by zero"

list_answer = []
test_cases = int(input())

for i in range(test_cases):
    list_int = []
    str_input = input()
    str_list = str_input.split(" ")
    for val in str_list:
        try:
            list_int.append(int(val))
        except ValueError as e:
            list_int.append(val)


    ans = except_test(list_int[0], list_int[1])
    list_answer.append(ans)

for i in list_answer:
    print(i)
