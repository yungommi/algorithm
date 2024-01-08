'''k=5
aa = [0 for _ in range(k)]
print(aa)'''

from itertools import combinations_with_replacement as cwr
from collections import Counter

def solution(n, info) :
    answer = []
    info = info[::-1] #0점짜리부터 
    max_n = -1
    k = len(info) #11 
    
    for c in cwr(range(0, k), n) : #0부터10을 중복허용해서 n번 뽑음
        ryan = 0
        apeach = 0
        tmp_ans = [0 for _ in range(k)] #tmp_ans = [0,0,0,0,0,0,0,0,0,0,0] len=11 
        
        c = Counter(c) #{0:2, 1:3, 5:3, ...}
        for i in range(0, k) : #(0~10)
            if info[i] < c[i] : # 개수가 더 많으면 라이언이 승
                ryan += i
            elif info[i] != 0 : # 아니면 어피치가 승
                apeach += i

            tmp_ans[i] = c[i]
        if ryan > apeach :
            diff = ryan - apeach
            if max_n < diff :
                max_n = diff
                answer = tmp_ans

    if answer :
        return answer[::-1]
    else :
        return [max_n]
