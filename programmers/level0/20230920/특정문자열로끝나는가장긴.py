# 예상 시간복잡도: O(n)

def solution(myString, pat):
    my_ = "".join(reversed(myString))
    pa_ = "".join(reversed(pat))
    new = my_[my_.find(pa_):]
    return "".join(reversed(new))


