#예상시간복잡도 : O(N * x = N)

import sys
input = sys.stdin.readline

orig = input().rstrip()
x = input().rstrip() 

st = []
ll = len(x)
for i in range(len(orig)):
    st.append(orig[i])
    if ''.join(st[-ll:]) == x:
        for _ in range(ll):
            st.pop()
if st:
    print(''.join(st))
else:
    print('FRULA')

'''
시간초고ㅏ ~~
import sys
input = sys.stdin.readline

orig = input().rstrip()
bomb = input().rstrip() 

while True:
    new = ''.join(orig.split(bomb))
    #print(new)
    if new == orig:
        print(new)
        break
    elif not new:
        print('FRULA')
        break
    else:
        orig = new 
'''