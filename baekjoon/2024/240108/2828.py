'''https://www.acmicpc.net/problem/2828'''

import sys
input = sys.stdin.readline

def main():
    n,m = map(int, input().split())
    num = int(input())

    loc = [1,m]
    ans = 0  

    for i in range(num):
        new = int(input())
        if new >= loc[0] and new <= loc[1]:
            pass
        else:
            ans += min(abs(new-loc[0]) , abs(new-loc[1]))
            if abs(new-loc[0]) < abs(new-loc[1]):
                loc[0] = new
                loc[1] = new+m-1
            else:
                loc[1] = new
                loc[0] = new-m+1
    return ans

print(main())