#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sum_list = []
    for i in range(1, len(arr)-1):
        for j in range(len(arr)-1):
            sum = arr[i][j] + arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1] 
            sum_list.append(sum)
    return(max(sum_list))

# sum = []


# for i in range(len(arr)-2):
#     for j in range(len(arr)-2):
#         sum.append(arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
        
# print(max(sum))

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # arr = []

    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))

    # result = hourglassSum(arr)

    # print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()

    test = [[-1, 1, -1, 0, 0, 0],
            [0, -1, 0, 0, 0, 0],
            [-1, -1, -1, 0, 0, 0],
            [0, -9, 2, -4, -4, 0],
            [-7, 0, 0, -2, 0, 0],
            [0, 0, -1, -2, -4, 0]]

    result = hourglassSum(test)

    print(result)


    test2 = [[0, 6,-7, 1, 6, 3],
            [-8, 2, 8, 3, -2, 7],
            [-3, 3,-6, -3, 0,-6],
            [5, 0, 5, -1, -5, 2],
            [6, 2, 8, 1, 3, 0],
            [8, 5, 0, 4, -7, 4]]
    
    result2 = hourglassSum(test2)

    print(result2)