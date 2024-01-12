# 예상 시간복잡도: O(N)

def solution(participant, completion):
    dict_ = {}
    for x in participant:
        if x in dict_:
            dict_[x]+=1
        else:
            dict_[x] = 1
    for x in completion:
        dict_[x] -= 1
        
    for x in dict_:
        if dict_[x] != 0 :
            return (x)
        else:
            pass

        