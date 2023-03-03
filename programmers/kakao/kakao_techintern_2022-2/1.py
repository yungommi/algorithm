a = max((1,5))
print(a)

#!/bin/python3

import math
import os
import random
import re
import sys


from itertools import combinations

def solution(cost, x):
    cost_= {}
    for i in range(len(cost)):
        cost_[cost[i]] = [i, 2**i]
    print(cost_)
    
    combi = []
    for n in range(1, len(cost)+1):
        combi += list(combinations(cost,n))
        print(list(combinations(cost,n)))
    
   
    return 0 

cost = [3,4,1]
x = 8

solution(cost,x)
