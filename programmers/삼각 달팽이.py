def solution(n):
    answer = [[0]*n for _ in range(n)]

    i = 0
    j = 0
    num = 1
    status = 0
    for s in range(n, 0, -1):
        if status == 0:
            if s != n:
                i += 1
            for k in range(s):
                answer[i][j]= num
                if k != s - 1:
                    i += 1
                num += 1
            status = (status+1) % 3
        elif status == 1:
            j += 1
            for k in range(s):
                answer[i][j] = num
                if k != s - 1:
                    j += 1
                num += 1
            status = (status+1) % 3
        elif status == 2:
            i -= 1
            j -= 1
            for k in range(s):
                answer[i][j] = num
                if k != s - 1:
                    i -= 1
                    j -= 1
                num += 1
            status = (status+1) % 3
    tmp = sum(answer, [])
    answer.clear()
    for t in tmp:
        if t != 0:
            answer.append(t)
    return answer