from collections import deque

def solution(rows, columns, queries):
    answer = []

    a = [[0]*columns for _ in range(rows)]
    num = 1

    for i in range(rows):
        for j in range(columns):
            a[i][j] = num
            num += 1
    
    for t in range(len(queries)):
        temp = []
        x1, y1, x2, y2 = queries[t]
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1

        for j in range(y1, y2):
            temp.append(a[x1][j])
        for i in range(x1, x2):
            temp.append(a[i][y2])
        for j in range(y2, y1, -1):
            temp.append(a[x2][j])
        for i in range(x2, x1, -1):
            temp.append(a[i][y1])
        answer.append(min(temp))
        temp = deque(temp)
        temp.rotate()
        k = 0
        for j in range(y1, y2):
            a[x1][j] = temp[k]
            k += 1
        for i in range(x1, x2):
            a[i][y2] = temp[k]
            k += 1
        for j in range(y2, y1, -1):
            a[x2][j] = temp[k]
            k += 1
        for i in range(x2, x1, -1):
            a[i][y1] = temp[k]
            k += 1

    return answer