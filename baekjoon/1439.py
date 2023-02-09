def function(s:str):
    answer = 0
    ss = s[0]
    tmp = s[0]
    for x in s: 
        if x != tmp:
            ss += x
        tmp = x
    return len(ss)//2

a = '0001100'
b = '11111'
c = '0000001'
d = '11001100110011000001'
e = '11101101'

print(function(a))
print(function(b))
print(function(c))
print(function(d))
print(function(e))