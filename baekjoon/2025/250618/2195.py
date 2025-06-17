#예상시간복잡도 : O(N)
import sys
input = sys.stdin.readline

S = input().strip()
P = input().strip()
index_p = 0
ans = 0

while index_p < len(P):
    max_value, temp, index_s = 0, 0, 0
    while index_s < len(S) and index_p + temp < len(P):
        if P[index_p + temp] == S[index_s]:
            temp += 1
            max_value = max(max_value, temp)
        else:
            temp = 0
        index_s += 1
    index_p += max_value
    ans += 1
print(ans)
