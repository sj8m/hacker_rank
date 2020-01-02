#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for x in range(n):
        y = x + 1
        total_whitespace = n - y
        result = ''
        for _ in range(total_whitespace):
            result += ' '
        for _ in range(y):
            result += '#'
        print(result)
        

if __name__ == '__main__':
    n = int(input())

    staircase(n)
