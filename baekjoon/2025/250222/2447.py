#예상 시간복잡도 O(N^2) 
#N=inp/ 재귀 depth : D=log(inp,3) /T(D)=O(9**0)+O(9**1)+...+O(9**D) = 9**D = 9**(log(inp,3) = inp^2)

import sys
input = sys.stdin.readline
import math

inp = int(input())
N = round(math.log(inp,3)) 
'''
int()를 사용하면 안됨
math.log()는 부동소수점 연산을 사용하으로 정확히 3의 제곱꼴이어도 오차가 발생한다. 27=>2.99..
정수로 변환하면 버림을 하여 실행오류 

'''
dic = [[] for _ in range(N+1)]
dic[0] = ["*"]

def function(N):
    if dic[N]==[]:
        orig = function(N-1)
        tmp = [["" for _ in range(3**N)] for _ in range(3**N)] 
        #deep copy 해야함 shallow copy하면 밑에 빵꾸뚫을때 전부 바뀜 
        for i in range(3):
            for j in range(3):
                for x in range(3**(N-1)):
                    for y in range(3**(N-1)):
                        tmp[i*(3**(N-1))+x][j*(3**(N-1))+y] = orig[x][y]
        for a in range(3**(N-1),3**(N-1)*2):
            for b in range(3**(N-1),3**(N-1)*2):
                tmp[a][b]=" "
        dic[N] = tmp
    return dic[N]

ans = function(N)
for i in range(inp):
    line = "".join(ans[i])
    print(line)