# 예상 시간복잡도: O(1)


from math import gcd
def solution(a, b):
    b //= gcd(a,b)   #b를 a와b의 최대공약수로 나눔 
    while b%2==0:
        b//=2
    while b%5==0:
        b//=5
    if b==1:
        return 1 
    else:
        return 2

