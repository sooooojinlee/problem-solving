
from collections import Counter

def solution(X, Y):
    answer = ''
    
    X = list(X)
    Y = list(Y)
    
    cntr_x = Counter(X)
    cntr_y = Counter(Y)
    common = cntr_x & cntr_y
    
    if len(common) == 0:
        answer += '-1'
        return answer
    
    if len(common) == 1 and common['0'] > 0:
        answer += '0'
        return answer
    
    common = sorted(common.items(), key = lambda item:item[0], reverse=True)
    print(common)
    
    for k, v in common:
        print(k, v)
        answer += (k*int(v))

    return answer

