# Given two strings s and t , write a function to determine if t is an anagram of s.

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    list_s = []
    list_t = []
    for i in s:
        list_s.append(i)
    for j in t:
        list_t.append(j)
    
    i = 0
    length_list = len(list_s)
    while length_list:
        if list_s[i] in list_t:
            print(list_t)
            print(list_s)
            list_t.remove(list_s[i])
            list_s.remove(list_s[i])
            length_list -= 1
        else:
            return False
    return True



    # word_t = {}
    # for i in t:
    #     if i in word_t:
    #         word_t[i] += 1
    #     else:
    #         word_t[i] = 1
        
    
if __name__ == "__main__":
    y = "asd"
    x = 'das'
    print(isAnagram(x, y))

    #return 2
    a = 'loveleetcode'
    z = 'loveleet'
    print(isAnagram(a, z))

    