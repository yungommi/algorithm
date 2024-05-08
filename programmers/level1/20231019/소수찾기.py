# 예상 시간복잡도: O(N^2)

def solution(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False 
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    count = primes.count(True)
    return count