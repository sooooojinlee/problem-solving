
def is_prime(n):
    if n <= 1: return False
    i = 2
    
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    
    return True


def solution(n, k):
    answer = 0
    
    t = [] # k진수로 변환
    
    while n > 0:
        t.append(n % k)
        n = n // k
    t.reverse()
    t = ''.join(map(str, t))

    t = t.split('0')
    
    for i in t:
        if i == '': continue
        i = int(i)
        if is_prime(i):
            answer += 1
    return answer

print(solution(110011, 10))