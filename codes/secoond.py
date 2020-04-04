#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':                          #1
    n = int(input())                                #2
                                                    #3
    arr = list(map(int, input().rstrip().split()))
    (arr.reverse())

    print(arr) #4
    for i in range(n):                              #5
        print(arr[i],end=' ')
