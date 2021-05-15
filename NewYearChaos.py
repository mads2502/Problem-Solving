#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    min_bribes=0
    for i in range(len(q)-1,-1,-1):
        
        bribe_here=q[i]-(i+1)
        #print(bribe_here,q[i])
        if(bribe_here>2):
            print("Too chaotic")
            return 
        else:
            if(i+1==q[i-1]):
                q[i],q[i-1]=q[i-1],q[i]
                min_bribes+=1
            elif(i+1==q[i-2]):
                q[i-2],q[i-1]=q[i-1],q[i-2]
                q[i],q[i-1]=q[i-1],q[i]
                min_bribes+=2
    print(min_bribes)
    return        

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
