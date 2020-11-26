# https://www.hackerrank.com/challenges/python-tuples/forum

# Given an integer,n , and  n space-separated integers as input,
# create a tuple, t , of those  integers. Then compute and print the result of hash(t).

n = int(input()) #number of inputs

l = input() # a string of space sperated numbers

str_list = l.split(' ') #split each string value into a list item at blank space

int_list = [int(n) for n in str_list] #use list comprehension to make each item an int

tup_list = tuple(int_list) #only immutable objects are hashable

print(hash(tup_list))