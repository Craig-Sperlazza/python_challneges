# Task
# Given  names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. 
# You will then be given an unknown number of names to query your phone book for. 

# # Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

friend_dict = {}

def make_dict():
    name_num = input()
    name_num_list = name_num.split(" ")
    # print(name_num_list)
    friend_dict[name_num_list[0]] = name_num_list[1]
    # print(friend_dict)

def check_dict(dict_input, key_name):
    if key_name in dict_input:
        return f"{key_name}={dict_input[key_name]}"
        
    else:
        return "Not found"
        

for i in range(n):
    make_dict()

name_check = ''
while True:
    try:
        name_check = input()
    except EOFError:
        break
    if name_check == '':
        break
    else:
        print(check_dict(friend_dict, name_check))
