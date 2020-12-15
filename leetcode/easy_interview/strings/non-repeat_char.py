# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

def firstUniqChar(s: str) -> int:
    #establish a dictionary containing each letter as a key with a value of its count frequency
    count_dict = {}  
    for i in range(len(s)):
        item = s[i]
        # print(item)
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    print(count_dict)

    #since the dictionary is unordered, we need to loop back through the string and stop once you hit the first key = 1
    index = 0 
    for letter in s:
        if count_dict[letter] == 1:
            return index
        else:
            index += 1
    return -1



if __name__ == "__main__":
    #return 0
    x = 'leetcode'
    print(firstUniqChar(x))

    #return 2
    y = 'loveleetcode'
    print(firstUniqChar(y))

    #return -1
    z = 'llaarr'
    print(firstUniqChar(z))