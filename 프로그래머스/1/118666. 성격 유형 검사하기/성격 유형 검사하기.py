def solution(survey, choices):
    answer = ""
    dic_ = {}
    # RTCFJMAN
    for i in 'RTCFJMAN':
        dic_[i] = 0

    for idx, v in enumerate(choices):
        if v == 7:
            type_ = survey[idx][1]
            dic_[type_] += 3
        elif v == 6:
            type_ = survey[idx][1]
            dic_[type_] += 2
        elif v == 5:
            type_ = survey[idx][1]
            dic_[type_] += 1
        elif v == 4:
            pass
        elif v == 3:
            type_ = survey[idx][0]
            dic_[type_] += 1
        elif v == 2:
            type_ = survey[idx][0]
            dic_[type_] += 2
        elif v == 1:
            type_ = survey[idx][0]
            dic_[type_] += 3
        
    for i in ["RT", "CF", "JM", "AN"]:
        if dic_[i[0]] >= dic_[i[1]]:
            answer += i[0]
        else:
            answer += i[1]

    return answer