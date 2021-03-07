#!/bin/python3

import math
import os
import random
import re
import sys

# Solution:
def sockMerchant(n, ar):
    #dictionary datastructure is the easiest way to do it
    l=dict()
    for item in ar:
        if item in l:
            l[item]+=1
        else :
            l[item]=1
    count=int(0)
    for key in l.keys():
        x=int(0)
        if l.get(key)%2==0:
            x=l.get(key)/2
        else:
            x=(l.get(key)-1)/2
        count+=x
    return int(count)
            
            
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
