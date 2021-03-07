#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    #
    n=n+1 if n%2==0 else n
    front=p
    back=n-p  
    length=1
    if front<back:
        length=front
    else:
        length=back
    turn=length/2
    
    return int(turn)
    #another technique
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
