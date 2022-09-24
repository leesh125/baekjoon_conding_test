def solution(v):
    answer = []
    dicx = {}
    dicy = {}

    for e in v:
        x,y = e
        if x not in dicx:
            dicx[x] = 1
        else:
            dicx[x] += 1
        if y not in dicy:
            dicy[y] = 1
        else:
            dicy[y] += 1

    for x in dicx:
        if dicx[x] == 1:
            answer.append(x)
            break
    for y in dicy:
        if dicy[y] == 1:
            answer.append(y)
    return answer