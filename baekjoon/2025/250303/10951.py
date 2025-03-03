#예상 시간복잡도 O(1)

import sys
input = sys.stdin.readline

while True:
    try:
        A,B = map(int,input().split())
        print(A+B)
    except:
        break
    
