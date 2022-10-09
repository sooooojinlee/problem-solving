import datetime
import math 

def solution(fees, records):
    answer = []
    
    d = dict()
    for r in records:
        t, number, status = r.split(' ')
        if number not in d.keys():
            d[number] = [t, status]
        else:
            d[number] += [t, status]

    d = dict(sorted(d.items()))
    
    for k in d.keys():
        if d[k][-1] == 'IN':
            d[k] += ['23:59', 'OUT']

        cur_fee = 0
        minute_sum = 0
        for i in range(0, len(d[k]), 4):
            h2, m2 = d[k][i+2].split(':')
            h1, m1 = d[k][i].split(':')
            
            t1 = datetime.timedelta(hours=int(h1), minutes=int(m1))
            t2 = datetime.timedelta(hours=int(h2), minutes=int(m2))
            
            hour, minute, _ = str(t2-t1).split(':')
            minute_sum += int(minute)
            minute_sum += (int(hour) * 60)
    
        if minute_sum > fees[0]:
            cur_fee += (fees[1] + (math.ceil((minute_sum - fees[0]) / fees[2])) * fees[3])
        else:
            cur_fee = fees[1]

        answer.append(cur_fee)
        
    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))