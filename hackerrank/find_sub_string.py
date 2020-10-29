# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

# NOTE: String letters are case-sensitive.

# Input Format

# The first line of input contains the original string. The next line contains the substring.

# Output Format

# Output the integer number indicating the total number of occurrences of the substring in the original string.

# Sample Input
# ABCDCDC
# CDC

# Sample Output
# 2

def count_substring(string, sub_string):
    ss_len = len(sub_string)
    s_len = len(string)
    count = 0

    for i in range(s_len):
        if string[i:i+ss_len] == sub_string:
            count += 1
    return count

#this wont work bnecause it does not count overlapping strings
def count_substring_method(string, sub_string):
    count = string.count(sub_string)
    return count



if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

    # string2 = input().strip()
    # sub_string2 = input().strip()

    # count2 = count_substring_method(string2, sub_string2)
    # print(count2)