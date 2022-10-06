
def solution(s):
    answer = []
    s = s[2:-2]
    s = list(s.split('},{'))
    s = sorted(s, key = lambda x: len(x))
    
    for c in s:
        c = list(map(int, c.split(',')))
        for x in c:
            if x not in answer:
                answer.append(x)
    return answer
