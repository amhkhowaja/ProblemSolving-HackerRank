#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def get_hourglass(arr:list,row :int, col:int ) ->list:
    hourglass=[[arr[row][col],arr[row][col+1],arr[row][col+2]],[0,arr[row+1][col+1],0],[arr[row+2][col],arr[row+2][col+1],arr[row+2][col+2]]]
    return hourglass
    
def tsum(hourglass:list)->int:
    total=0
    for i in range(3):
        for j in range(3):
            total+=hourglass[i][j]
    return total
def hourglassSum(arr): #Implementation
    sums=[]
    for i in range(0,4):
        tempsum=0
        for j in range(0,4):
            #extract all the hourglasses and simultaneously sum them into sums list.
            hg=get_hourglass(arr,i,j)
            tempsum=tsum(hg)
            sums.append(tempsum)
    #Determine the max sum:
    big=sums[0]
    for number in sums:
        if number>big:
            big=number
    return big
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
