#예상시간복잡도 : O(N)

import sys 
input = sys.stdin.readline 
S = set()
def function(str):
    global S
    l = list(str.split())
    if len(l)==1:
        a = l[0]
    else:
        a = l[0]
        n = int(l[1])

    if a == "add":
        S.add(n)
    elif a == "remove":
        S.discard(n)
        #discard는 아이템 없어도 에러 안남 
        #remove는 에러
    elif a == "check":
        if n in S:
            print(1)
        else:
            print(0)
        pass
    elif a == "toggle":
        if n in S:
            S.remove(n)
        else:
            S.add(n)
    elif a == "all":
        S = set(range(1,21))
    elif a == "empty":
        S.clear()

n = int(input())
for _ in range(n):
    str = input().rstrip()
    function(str)
