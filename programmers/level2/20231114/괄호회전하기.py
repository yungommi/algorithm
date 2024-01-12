# 예상 시간 복잡도 O(n^2)

def solution(s):
    count=0
    for i in range(len(s)):
        tmp=s[i:]+s[:i]
        while True:
            length=len(tmp)
            tmp=tmp.replace("()","")
            tmp=tmp.replace("{}","")
            tmp=tmp.replace("[]","")
            if len(tmp)==0:
                count+=1
                break 
            if length==len(tmp): 
                break
    return count

