# 예상 시간복잡도: O(N^2)

def solution(dartResult):
    g = []
    n = -1
    tmp = 0
    for x in dartResult:
        if tmp==0 and x.isdigit():
            g.append(int(x)) 
            n+= 1
            tmp = int(x)
        elif tmp and x.isdigit():
            g[n] = 10*tmp + int(x)
            tmp = g[n]
        else:
            tmp = 0
            if x=='*':
                    g[n] *= 2
                    if n>0:
                        g[n-1]*=2
            elif x=='#':
                g[-1] *= -1
            elif x=='S':
                pass
            elif x=='D':
                g[n] = g[n]**2
            elif x=='T':
                g[n]= g[n]**3
    return sum(g)

