#예상시간복잡도 : O(N^3)
import sys
import math 
input = sys.stdin.readline


x = input().rstrip()
a_min = math.inf
a_max = 0 

def calc(n:str):
    ans = 0 
    for N in n:
        if int(N)%2 != 0:
            ans += 1 
    return ans 

def function(n, oddnum):
    global a_min, a_max 
    if len(n)==1:
        a_min = min(a_min, oddnum)
        a_max = max(a_max, oddnum)
    elif len(n)==2:
        tmp = str(int(n[0])+int(n[1]))
        function(tmp, oddnum + calc(tmp))
    else:
        for i in range(len(n)-2):
            for j in range(i+1,len(n)-1):
                a = n[:i+1]
                b = n[i+1:j+1]
                c = n[j+1:]
                tmp = str(int(a)+int(b)+int(c))
                function(tmp, oddnum + calc(tmp)) 


function(x, calc(x))
print(a_min, a_max)


