'''
N개의 스위치와 N개의 전구가 있다. 각각의 전구는 켜져 있는 상태와 꺼져 있는 상태 중 하나의 상태를 가진다. 
i(1 < i < N)번 스위치를 누르면 i-1, i, i+1의 세 개의 전구의 상태가 바뀐다. 
즉, 꺼져 있는 전구는 켜지고, 켜져 있는 전구는 꺼지게 된다. 1번 스위치를 눌렀을 경우에는 1, 2번 전구의 상태가 바뀌고, N번 스위치를 눌렀을 경우에는 N-1, N번 전구의 상태가 바뀐다.

N개의 전구들의 현재 상태와 우리가 만들고자 하는 상태가 주어졌을 때, 그 상태를 만들기 위해 스위치를 최소 몇 번 누르면 되는지 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(2 ≤ N ≤ 100,000)이 주어진다. 
다음 줄에는 전구들의 현재 상태를 나타내는 숫자 N개가 공백 없이 주어진다. 
그 다음 줄에는 우리가 만들고자 하는 전구들의 상태를 나타내는 숫자 N개가 공백 없이 주어진다. 0은 켜져 있는 상태, 1은 꺼져 있는 상태를 의미한다.

출력
첫째 줄에 답을 출력한다. 불가능한 경우에는 -1을 출력한다.
inp>>
3
000
010
out>>
3
'''

#예상시간복잡도 : O(NQ)

import sys
input = sys.stdin.readline
#sys.setrecursionlimit(10**6)

def function1(tar, cur):
  st = 0 
  ans = 0 
  while st<=N-1:
    if st== 0 :
      cur[st] = 1 if cur[st]==0 else 0 
      cur[st+1] = 1 if cur[st+1]==0 else 0
      ans += 1 
    elif st == N-1: 
      if cur[st-1] == tar[st-1]:
        pass
      else:
        cur[st-1] = 1 if cur[st-1]==0 else 0 
        cur[st] = 1 if cur[st]==0 else 0
        ans += 1 
    else:
      if cur[st-1] == tar[st-1]:
        pass
      else:
        cur[st-1] = 1 if cur[st-1]==0 else 0 
        cur[st] = 1 if cur[st]==0 else 0 
        cur[st+1] = 1 if cur[st+1]==0 else 0 
        ans += 1
    st += 1 
  if cur[N-1]==tar[N-1]:
    return ans
  else:
    return -1
  
def function2(tar, cur):
  st = 1
  ans = 0 
  while st<=N-1:
    if st == N-1: 
      if cur[st-1] == tar[st-1]:
        pass
      else:
        cur[st-1] = 1 if cur[st-1]==0 else 0 
        cur[st] = 1 if cur[st]==0 else 0
        ans += 1 
    else:
      if cur[st-1] == tar[st-1]:
        pass
      else:
        cur[st-1] = 1 if cur[st-1]==0 else 0 
        cur[st] = 1 if cur[st]==0 else 0 
        cur[st+1] = 1 if cur[st+1]==0 else 0 
        ans += 1
    st += 1 
  if cur[N-1]==tar[N-1]:
    return ans
  else:
    return -1

N = int(input())
target = list(map(int, input().rstrip()))
current = list(map(int, input().rstrip()))
f1 = function1(target[:],current[:])
f2 = function2(target[:],current[:])
if f1==-1 or f2==-1:
  print(max(f1, f2))
else:
  print(min(f1, f2))


print(current)
