#예상시간복잡도 : O(N*M) N:문자열 수 M:length of 문자열

import sys
input = sys.stdin.readline

def function(str):
    n = len(str)
    for i in range(n):
        if str[i]==str[n-i-1]:
            pass
        else:
            return("no")
    return("yes")

while True:
    str = input().rstrip()
    if str == '0':
        break
    else:
        print(function(str))

