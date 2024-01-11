'''https://www.acmicpc.net/problem/2870'''

import sys
import re
input = sys.stdin.readline
n= int(input())
ans = []

for i in range(n):
    inp = input()
    numbers = re.findall(r'\d+', inp)
    numbers = list(map(int,numbers))
    ans += numbers

ans.sort()
for x in ans:
    print(x)