# 2108 

from collections import Counter 
import sys

n = int(sys.stdin.readline())
l = [0]*n
for i in range(n):
    tmp = int(sys.stdin.readline())
    l[i] = tmp

l.sort()
cnt = Counter(l).most_common(2)

print(round(sum(l)/n))
print(l[(n)//2])
if len(cnt) == 1:
    print(l[0])
else:
    if cnt[0][1] > cnt[1][1]:
        print(cnt[0][0])
    else:
        print(cnt[1][0])
print(l[-1]-l[0])