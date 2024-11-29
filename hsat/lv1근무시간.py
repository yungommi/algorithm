import sys
input = sys.stdin.readline 

ans = 0
for i in range(5):
    inp = input()
    ans += (int(inp[6:8])*60 + int(inp[9:11]) - int(inp[0:2])*60 - int(inp[3:5]))

print(ans)