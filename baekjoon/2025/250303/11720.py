# 예상시간복잡도 : O(n)

import sys 
input = sys.stdin.readline

N = int(input())
nums = input().rstrip()
ans = 0 
for x in range(N):
    ans += int(nums[x])

print(ans) 

