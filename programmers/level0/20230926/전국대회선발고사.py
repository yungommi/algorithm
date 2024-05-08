# 예상 시간복잡도: O(n)

def solution(rank, attendance):
    tmp=[]
    for i in range(len(rank)):
        if attendance[i]==True:
            tmp.append([rank[i],i])
    tmp.sort()
    return tmp[0][1]*10000 + tmp[1][1]*100 + tmp[2][1]


