def solution(maps):
    answer = 0
    n=(len(maps))
    m=len(maps[1])
    a=0
    b=0
    maps[0][0]= 'x'
    while not(maps[n-1][m-1]=='x'):
        if (a+1<n) and maps[a+1][b]==1 :
            a+=1 
            maps[a][b] = 'x'
        elif (b+1<m) and maps[a][b+1]==1:
            b+=1 
            maps[a][b] = 'x'
        elif (a-1 >= 0) and maps[a-1][b]==1 :
            a-=1 
            maps[a][b] = 'x'
        elif (b-1 >=0) and maps[a][b-1]==1 :
            b-=1 
            maps[a][b] = 'x'
        else:
            return -1
    for i in maps:
        for j in i:
            if j == 'x':
                answer += 1
    return answer