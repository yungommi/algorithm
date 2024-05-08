# 예상 시간복잡도: O(n)

def solution(binomial):
    l_ = binomial.split()
    print(l_)
    if l_[1]=='+':
        return int(l_[0]) + int(l_[2])
    elif l_[1]=='-':
        return int(l_[0]) - int(l_[2])
    else:
        return int(l_[0]) * int(l_[2])
    
