#예상 시간복잡도 O(n) ? math.factorial의 시간복잡도?

import sys
input = sys.stdin.readline
import math

A,B = map(int, input().split())

ans = math.factorial(A)//(math.factorial(B)*math.factorial((A-B)))
print(ans)
