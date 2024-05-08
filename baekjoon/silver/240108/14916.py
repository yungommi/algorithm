'''https://www.acmicpc.net/problem/14916'''

import sys
input = sys.stdin.readline

def main(money):
    q,r = divmod(money,5)
    if r%2 ==0 :
        return q+(r//2)
    else:
        ans = 0 
        while money>0:
            money -= 2 
            ans += 1
            if money %5 == 0 :
                return ans + money//5
        return -1

money = int(input())
print(main(money))

