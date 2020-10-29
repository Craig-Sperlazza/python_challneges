"""
Input Format

A single line containing a string .

Constraints


Output Format

In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
In the second line, print True if  has any alphabetical characters. Otherwise, print False.
In the third line, print True if  has any digits. Otherwise, print False.
In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
"""

#python has a built in any() function that returns true if any evaluate to true
def is_any_string(string):

    print(any(c.isalnum() for c in string))
    print(any(c.isalpha() for c in string))
    print(any(c.isdigit() for c in string))
    print(any(c.islower() for c in string))
    print(any(c.isupper() for c in string))




def string_validators(string):
    count = False

    # In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
    for i in string:
        if i.isalnum():
            count = "True"
            print("True")
            break 
        else:
            continue
    if count == False:
        print("False")
    else:
        count = False
    
    # In the second line, print True if  has any alphabetical characters. Otherwise, print False.
    for i in string:
        if i.isalpha():
            count = "True"
            print("True")
            break 
        else:
            continue
    if count == False:
        print("False")
    else:
        count = False
    
    # In the third line, print True if  has any digits. Otherwise, print False.
    for i in string:
        if i.isdigit():
            count = "True"
            print("True")
            break 
        else:
            continue
    if count == False:
        print("False")
    else:
        count = False
    
    # In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
    for i in string:
        if i.islower():
            count = "True"
            print("True")
            break 
        else:
            continue
    if count == False:
        print("False")
    else:
        count = False
    
    # In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
    for i in string:
        if i.isupper():
            count = "True"
            print("True")
            break 
        else:
            continue
    if count == False:
        print("False")
    else:
        count = False




if __name__ == '__main__':
    s = input()
    string_validators(s)
    is_any_string(s)