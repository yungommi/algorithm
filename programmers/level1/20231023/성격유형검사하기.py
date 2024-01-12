# 예상 시간복잡도: O(N)

def solution(survey, choices):
    answer = ''
    dict = {'A': 0 ,'N':0, 'C':0, 'F':0, 'M':0, 'J':0, 'R':0, 'T':0}
    for i in range (len(survey)):
        if choices[i]>4:
            dict[survey[i][1]] += (choices[i]-4)
        else:
            dict[survey[i][0]] += (4-choices[i])
            
    if dict['R']< dict['T']:
        answer += 'T'
    else: 
        answer += 'R'
        
    if dict['C']< dict['F']:
        answer += 'F'
    else: 
        answer += 'C'
        
    if dict['J']< dict['M']:
        answer += 'M'
    else: 
        answer += 'J'
        
    if dict['A']< dict['N']:
        answer += 'N'
    else: 
        answer += 'A'
    
    return answer

