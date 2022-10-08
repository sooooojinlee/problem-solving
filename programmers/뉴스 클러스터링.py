
from collections import Counter

def solution(str1, str2):
    answer = 0
    
    str1_lst = []
    str2_lst = []
    str1 = str1.upper()
    str2 = str2.upper()

    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            str1_lst.append(str1[i:i+2])

    
    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            str2_lst.append(str2[i:i+2])

    
    str1_cntr = Counter(str1_lst)
    str2_cntr = Counter(str2_lst)
    
    if len(str1_lst) + len(str2_lst) == 0:
        return 65536
    intersection = sum((str1_cntr & str2_cntr).values())
    union = sum((str1_cntr | str2_cntr).values())
    
    if intersection == 0 and union > 0:
        return 0
    answer = int((intersection / union) * 65536)
    
    return answer

print(solution("E=M*C^2", "e=m*c^2"))