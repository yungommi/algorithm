

list = [1, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

def function(n:int):
    if n<len(list):
        return list[n]
    else: 
        for i in range(11,n+1):
            list.append(list[i-1]+list[i-5])
        return list[n]

n= int(input())
l = [0 for i in range(n)]

for i in range(n):
    l[i] = int(input())

for x in l:
    print(function(x))