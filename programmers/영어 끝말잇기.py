
def solution(n, words):
    answer = []
    count = [0] * (n+1)
    history = []

    for i in range(len(words)):
        count[i%n+1] += 1
        if i == 0:
            history.append(words[i])
            continue
        if words[i-1][-1] != words[i][0]:
            answer.append(i%n+1)
            answer.append(count[i%n+1])
            break
        elif words[i] in history:
            answer.append(i%n+1)
            answer.append(count[i%n+1])
            break
        else:
            history.append(words[i])
    
    if len(answer) == 0:
        answer = [0, 0]

    return answer