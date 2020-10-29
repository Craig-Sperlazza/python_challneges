#!/bin/python3

import math
import os
import random
import re
import sys

def reverse_arr(arr):
    str_ints = [str(i) for i in arr]
    # print(str_ints)
    str_ints.reverse()
    string = " ".join((str_ints))
    return (string)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    # print(arr)
    print(reverse_arr(arr))