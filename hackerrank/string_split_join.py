# https://www.hackerrank.com/challenges/python-string-split-and-join/problem
# takes a string seperated by spaces and returns a string seperated by -

def split_and_join(line):
    split_lst = line.split(" ")
    join_str = "-".join(split_lst)
    print(join_str)

test = "I am coming home"

split_and_join(test)

split_and_join("this is a string")