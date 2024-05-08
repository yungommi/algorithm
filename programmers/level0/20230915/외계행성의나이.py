# 예상 시간복잡도: O(n)

def solution(age):
    answer = ''
    dict_ = {'0':'a', 
             '1':'b',
             '2':'c', 
             '3':'d',
             '4':'e',
             '5':'f',
             '6':'g',
             '7':'h',
             '8':'i',
             '9':'j'}
    age = str(age)
    for x in age:
        answer += dict_[x]
    return answer
