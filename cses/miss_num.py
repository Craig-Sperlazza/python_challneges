def makeOrderedList(strNum):
    new_lst = strNum.split(' ')
    int_lst = list(map(int, new_lst))
    int_lst.sort()
    #print(int_lst)
    return int_lst

def miss_num(n, arr):
    if n not in arr:
        return n
    elif len(arr) == 1:
        return 1
    for i in range(len(arr)-1):
        curr = arr[i]
        next = arr[i+1]
        gap = next - curr
        if gap == 2:
            return curr+1
    #return n
    
    

if __name__ == "__main__":
    finalNum = int(input())
    stringNum = input()
    
    list_of_int = makeOrderedList(stringNum)
    
    print(miss_num(finalNum, list_of_int))
    
    