#HACKERRANK DYNAMIC ARRAY UNDER PROBLEM SOLVING
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    #print(queries)
    arr = [[] for i in range(n)]
    answerarray=[]
    lastAnswer=0
    for query in queries:
        q=query
        for i in range(len(q)):
            q[i]=int(q[i])
        if q[0]==1:
            idx=((q[1]^lastAnswer)%n)
            arr[idx].append(q[2])
        elif q[0]==2:
            idx=((q[1]^lastAnswer)%n)
            lastAnswer=arr[idx][q[2]%len(arr[idx])]
            answerarray.append(lastAnswer)
    return answerarray
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
