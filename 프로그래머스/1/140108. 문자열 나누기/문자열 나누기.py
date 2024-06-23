def solution(s):
    answer = 0
    i = 1
    cntA = 1
    cntB = 0
    while len(s)>0:
        if len(s) == 1:
            answer += 1
            break
        else:
            x = s[0]
            if s[i] == x:
                cntA += 1
                i += 1
            else:
                cntB += 1
                i += 1
            if cntA > len(s)-cntA:
                answer += 1
                break
            if cntA == cntB:
                answer += 1
                s = s[cntA+cntB:]
                i = 1
                cntA = 1
                cntB = 0
    return answer