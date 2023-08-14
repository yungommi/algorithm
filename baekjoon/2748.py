'''피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.

이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.

n=17일때 까지 피보나치 수를 써보면 다음과 같다.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.'''



'''tmp = [0 for i in range(0,90)]
tmp[1]=1

def function(n:int):
    if tmp[n-1] == 0 and n>1:
        tmp[n-1]= function(n-1) + function(n-2)
    else:
        return tmp[n-1]
print(tmp)
print(function(n))'''

n = int(input())
def fib(n):
    fibList=[0, 1]
    if n<2 :
        return fibList[n]
    for i in range(2,n+1):
        fibList.append( fibList[i-1] + fibList[i-2] )
    return fibList[n]

print(fib(n))
