def solution(X, Y):
    answer = ''
    couple = []
    for i in range(10):
        tempX = X.count(str(i))
        tempY = Y.count(str(i))
        temp = min(tempX, tempY)
        for _ in range(temp):
            couple.append(i)
    if set(couple) == {0}:
        return '0'
    elif len(couple) == 0:
        return '-1'
    couple.sort(reverse=True)
    for i in couple:
        answer += str(i)
    return answer