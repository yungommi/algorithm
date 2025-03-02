#예상 시간복잡도 O(M)

import sys
input = sys.stdin.readline

inp = input().rstrip()

ans = 0
idx = 0 
while True:
    ans += 1 
    for s in str(ans):
        if inp[idx] == s:
            idx += 1 
            if idx >= len(inp):
                print(ans)
                exit()

    