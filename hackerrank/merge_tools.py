# https://www.hackerrank.com/challenges/merge-the-tools/problem?h_r=next-challenge&h_v=zen

def merge_the_tools(string, k):
    length = len(string)
    equal_parts = int(length // k)
    start = 0
    stop = equal_parts
    word_list = []
    
    #splits the string into a list of strings of length equal_parts
    for i in range(stop):
        string_seg = string[start:stop]
        word_list.append(string_seg)
        start += equal_parts
        stop += equal_parts
    
    # print(word_list)

    for word in word_list:
        #split each string group into its own list with each string letter being a sperate list item
        split_list = [char for char in word]
        #print(split_list)

        #remove all instances of duplicate letters (keys in a dictionary must be unique)
        my_unique_list = list(dict.fromkeys(split_list))
        #print(my_unique_list)

        #convert to string and print
        print(''.join(my_unique_list))
        



if __name__ == '__main__':

    merge_the_tools("AABCAAADA", 3)