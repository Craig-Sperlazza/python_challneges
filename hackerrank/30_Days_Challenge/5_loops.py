#!/bin/python3

import math
import os
import random
import re
import sys

#as a function
def n_times(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")



if __name__ == '__main__':
    n = int(input())
    #call function
    n_times(n)
    #list comprehension
    f_string = [print(f"{n} * {i} = {n*i}") for i in range(1, 11)]
    print(f_string)