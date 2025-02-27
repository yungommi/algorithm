#예상 시간복잡도 O(1)

import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()
c = input().rstrip()

if a.isdigit():
    n = int(a)+3
elif b.isdigit():
    n = int(b)+2
else:
    n = int(c)+1

if n % 3 == 0 :
    if n % 5 == 0:
        print("FizzBuzz")
    else:
        print("Fizz")
elif n%5==0:
    print("Buzz")
else:
    print(n)