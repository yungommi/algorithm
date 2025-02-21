# 2579
# dp

n = int(input())
s = [0]*301
for i in range(n):
    x = int(input())
    s[i+1] = x

def function(s,n):
  point = [0]* (301)
  point[1] = s[1]
  point[2] = s[1] + s[2]
  for x in range(3,n+1):
     point[x] = max(point[x-3]+s[x-1]+s[x], point[x-2]+s[x])
  return(point[n])

print(function(s,n))