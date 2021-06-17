#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#


#This peace of code is only for little number of queries small number of resultant---------> Working properly (You can Try)
#def arrayManipulation(n, queries):
#    # Write your code here
#    arr=[0]*(n+2)
#    for query in queries:
#        a=query[0]-1
#        b=query[1]-1
#        k=query[2]
#        for i in range(a,b+1):
#            arr[i]+=k
#    maximum=max(arr)
#    return maximum'''

def arrayManipulation(n, queries):
    arr=[0]*(n+1)
    for a,b, k in queries:
        arr[a-1]+=k                     #0+100=100
        arr[b]-=k                       #0-100=-100        we will sum each element to know if there is maximum number
    #Finding the maximum number out of the array
    sumvalue=0
    maximum =0
    for i in arr:
        sumvalue+=i
        maximum =max(sumvalue, maximum)  
    return maximum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
