#예상 시간복잡도 O(n) 

import sys
input = sys.stdin.readline
n = int(input())

inp = list(map(int, input().split())) 
inp.sort()
max = inp.pop()
max += sum(inp)/2

print(max)