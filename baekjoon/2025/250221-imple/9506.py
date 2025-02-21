#예상 시간복잡도 O(N) 

import sys
input = sys.stdin.readline

def function(n):
    l = []
    add = 0
    for i in range(1,n):
        if n%i==0: 
            add += i 
            l.append(str(i))
    if add == n :
        joined = " + ".join(l)
        print(n,"=",joined)
    else:
        print(n, "is NOT perfect.")

while True:
    k = int(input())
    if k == -1:
        break
    else:
        function(k)