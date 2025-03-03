#예상 시간복잡도 O(1)

import sys
input = sys.stdin.readline

N = int(input())

if N%4 == 0 :
    if N % 400 == 0:
        print(1)
    elif N % 100 != 0 :
        print(1)
    else:
        print(0)
else:
    print(0)
