def solution(name, yearning, photo):
    answer = list()
    mydict = dict()
    for i in range(len(name)):
        mydict[name[i]] = yearning[i]
    
    for names in photo:
        cnt = 0
        for n in names:
            if n not in mydict:
                pass
            else:
                cnt += mydict[n]
        answer.append(cnt)

    return answer