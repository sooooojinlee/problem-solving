
def solution(record):
    answer = []
    
    user = dict()
    
    for r in record:
        r = r.split(' ')
        if r[0] == 'Enter':
            user[r[1]] = [r[2], r[0]]
        elif r[0] == 'Leave':
            user[r[1]][1] = r[0]
        elif r[0] == 'Change':
            user[r[1]] = [r[2], r[0]]

    for r in record:
        r = r.split(' ')
        if r[0] == 'Enter':
            answer.append('{0}님이 들어왔습니다.'.format(user[r[1]][0]))
        elif r[0] == 'Leave':
            answer.append('{0}님이 나갔습니다.'.format(user[r[1]][0]))
        elif r[0] == 'Change':
            continue
    
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))