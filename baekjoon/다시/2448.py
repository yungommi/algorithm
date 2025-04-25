#예상시간복잡도 : O(K)
import sys
input = sys.stdin.readline
import math


N = int(input())
N = N//3 
N = int(math.log(N+1,2))
print(N)

l = 5 
h = 3
tree = [[' ',' ','*',' ',' '],[' ','*',' ','*',' '],['*','*','*','*','*']]

for i in range(N):
    for i in range(h):
        tmp = tree[i] + [' '] + tree[i] 
        tree.append(tmp)

    added = (l+1)//2
    for i in range(h):
        tmp = [' ']* added + tree[i] +[' ']* added
        tree[i] = tmp
    h *= 2 
    l = 2*l + 1

for x in tree:
    print(''.join(x))

