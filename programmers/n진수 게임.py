def solution(n, t, m, p):
    answer = ''
    temp = [0]
    d = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']

    for i in range(1, m*t):
        cur = []
        while i > 0:
            cur.append(d[i % n])
            i = i // n
        cur.reverse()
        temp += cur

    for k in range(p-1, m*t, m):
        answer += str(temp[k])

    return answer