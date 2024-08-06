#예상 시간복잡도 O(n) 
import sys
input = sys.stdin.readline
n = int(input())

for i in range(n):
	inp = str(input().strip())  # 줄바꿈 삭제~~ 
	pwd = [] 
	sub = [] 
	for a in inp:
		if a == '<': 
			if pwd: 
				sub.append(pwd.pop()) 
		elif a == '>': 
			if sub: 
				pwd.append(sub.pop()) 
		elif a == '-': 
			if pwd: 
				pwd.pop() 
		else:
			pwd.append(a) 
	print("".join(pwd)+"".join(sub[::-1]))
	

#예상 시간복잡도 O(n^2) 
import sys
input = sys.stdin.readline
from collections import deque 
n = int(input())

for i in range(n): 
    inp = str(input())
    d = deque() 

    cursor = 0 
    end = 0 

    for x in inp:
        if x == '<':
            cursor = max(0,cursor-1)
        elif x == '>':
            cursor = min(cursor+1, end)
        elif x == '-':
            if cursor>0:
                del d[cursor-1]  #O(n) 
                cursor -= 1
                end -= 1 
        else:
            d.insert(cursor, x)
            cursor += 1
            end += 1
    print("".join(list(d)))
