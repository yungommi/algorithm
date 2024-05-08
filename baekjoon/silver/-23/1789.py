'''서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?

입력
첫째 줄에 자연수 S(1 ≤ S ≤ 4,294,967,295)가 주어진다.

출력
첫째 줄에 자연수 N의 최댓값을 출력한다.'''

n = int(input())

def function(n:int):
    tmp = 0 
    add = 1
    while n>0:
        if n > add:
            n -= add
            add += 1
            tmp += 1
        else:
            return tmp
        
print(function(n))