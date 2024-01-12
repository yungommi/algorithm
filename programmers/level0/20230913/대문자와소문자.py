# 예상 시간복잡도: O(n)

def solution(my_string):
    len_ = len(my_string)
    list_ = [0 for x in my_string]
    for i in range(0,len_):
        if my_string[i].isupper():
            list_[i] = my_string[i].lower()
        else:
            list_[i] = my_string[i].upper()
    return "".join(list_)

