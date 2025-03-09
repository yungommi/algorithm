#예상시간복잡도 : O(N*M) N:문자열 수 M:length of 문자열

import sys
input = sys.stdin.readline
import math

A,B = map(int, input().split())

print(math.gcd(A,B)) #greatest common divisor 
print(math.lcm(A,B)) #largest common multiple

