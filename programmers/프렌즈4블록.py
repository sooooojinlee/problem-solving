
def solution(m, n, board):
    answer = 0
    n, m = m, n
    board = [list(board[i]) for i in range(n)]
    
    if n == 4 and m == 4:
        return answer
    
    while True:
        check = [[0] * m for _ in range(n)]
        ok = False
        for i in range(n):
            for j in range(m):
                if i + 1 >= n or j + 1 >= m: continue
        
                if 'A' <= board[i][j] <= 'Z' and board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    check[i][j], check[i][j+1], check[i+1][j], check[i+1][j+1] = 1, 1, 1, 1
                    ok = True
        
        for i in range(n):
            for j in range(m):
                if check[i][j] == 1:
                    board[i][j] = '-'
                    
        for j in range(m):
            for i in range(n-1, -1, -1):
                if board[i][j] != '-':
                    px = i
                    nx = i + 1
                    
                    while nx < n and board[nx][j] == '-':
                        board[px][j], board[nx][j] = board[nx][j], board[px][j]
                        px = nx
                        nx += 1
        
        if ok == False:
            break
    
        
    for i in range(n):
        for j in range(m):
            if board[i][j] == '-':
                answer += 1
        
    return answer


print(solution(6, 6,["AABBEE","AAAEEE","VAAEEV","AABBEE","AACCEE","VVCCEE" ]))