# 1463
# dp 

def dpdp(n:int):
  possible = [[n]]
  for x in range(1,n+1):
    new = find(possible[-1])
    if 1 in new:
       break
    else:
       possible.append(new)
  return len(possible)

def find(l):
    tmp = []
    for x in l:
        tmp.append(x-1)
        if x%2 == 0:
            tmp.append(x//2)
        if x%3 == 0:
            tmp.append(x//3)
    return list(set(tmp))

print(dpdp(10))

def dpdp1(n:int):
  l = [0]*(n+1)
  for i in range(2,n+1):
      l[i] = l[i-1]+1
      if i%2 == 0 :
        l[i] = min(l[i], l[i//2]+1)
      if i%3 == 0:
        l[i] = min(l[i], l[i//3]+1)
  return l[n]

print(dpdp1(10))