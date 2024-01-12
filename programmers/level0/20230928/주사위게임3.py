# 예상 시간복잡도: O(n)

def solution(a, b, c, d):
    tmp = [a,b,c,d]
    tmp.sort()
    a,b,c,d = tmp
    if a==b and b==c and c==d:
        return 1111*a 
    elif a==b and b==c:
        return (10*a + d)**2
    elif b==c and c==d:
        return (10*b + a)**2
    elif a==b and c==d:
        return (a+c)*(c-a)
    elif a==b:
        return c*d
    elif b==c:
        return a*d
    elif c==d:
        return a*b
    else:
        return a
        