#예상 시간복잡도 O(1)

import sys
input = sys.stdin.readline

N = int(input())

if N >= 90:
    print("A")
elif N >= 80 :
    print("B")
elif N >= 70:
    print("C")
elif N >= 60:
    print("D")
else:
    print("F")

    