#예상시간복잡도 : O(n)
import sys
input = sys.stdin.readline

data = []
for i in range(int(input())):
	x, y = map(int,input().split())
	data.append((x,y))

data.sort(key = lambda x : (x[1], x[0]))

for d in data:
	print(d[0], d[1])
	