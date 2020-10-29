return_list = []

def list_work(operation):
    global return_list
    split_list = operation.split(" ")
    # print(split_list)
    if split_list[0] == "insert":
        # insert i e ---insert integer e at position i
        insert_item(return_list, int(split_list[1]), int(split_list[2]))

    elif split_list[0] == "print":
        print(return_list)

    elif split_list[0] == "remove":
        remove_item(return_list, int(split_list[1]))

    elif split_list[0] == "append":
        # return_list = append_item(return_list, split_list[1])
        # print(return_list)
        append_item(return_list, int(split_list[1]))

    elif split_list[0] == "sort":
        return_list.sort()
    
    elif split_list[0] == "pop":
        return_list = return_list[:-1]

    elif split_list[0] == "reverse":
        return_list = return_list[::-1]

def append_item(lst, item):   
    return lst.append(item)

def remove_item(lst, item):   
    return lst.remove(item)

def insert_item(lst, pos, item):
    return lst.insert(pos, item)

if __name__ == '__main__':
    N = int(input())
    return_list = []
    for i in range(N):
        op = str(input())
        list_work(op)
    
