# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
# You are given  scores. Store them in a list and find the score of the runner-up.

def find_second(arr):
    #get rid of duplicates
    new_set = set(arr)
    new_arr = list(new_set)
    new_arr.sort()

    if len(new_arr) <= 2:
        return new_arr[0]
    else:
        return new_arr[-2]













if __name__ == "__main__":
    sample = [2, 3, 6, 6, 5]
    sample2 = [2, 2, 2, 2, 4]
    sample3 = [5, 7, 3, 2, 1]
    sample4 = [-1, -10, -4, 0]
    sample5 = [-4, -3, 0, 2]
    sample6 = [2, 2, 2, 2, 2, 2]

    print(find_second(sample))
    print(find_second(sample2))
    print(find_second(sample3))
    print(find_second(sample4))
    print(find_second(sample5))
    print(find_second(sample6))
