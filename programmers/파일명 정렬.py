


def solution(files):
    answer = []

    temp = []
    for file in files:
        ok = False
        head = ''
        number = ''
        tail = ''
        for i in range(len(file)):
            if ok == False and file[i].isdigit() == False:
                head += file[i]
            elif file[i].isdigit():
                number += file[i]
                ok = True
            else:
                tail = file[i:]
                break

        temp.append((head, number, tail))

    temp = sorted(temp, key=lambda x: (x[0].lower(), int(x[1])))

    for t in temp:
        answer.append(''.join(map(str, t)))

    return answer