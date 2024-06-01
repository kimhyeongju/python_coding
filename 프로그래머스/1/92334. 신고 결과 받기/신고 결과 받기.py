def solution(id_list, report, k):
    report = list(set(report))
    answer = [0]*len(id_list)
    active_list = []
    passive_list = []
    for i in report:
        active_list.append(i.split()[0])
        passive_list.append(i.split()[1])
    
    banned = []
    for i in id_list:
        cnt = passive_list.count(i)
        if cnt >= k:
            banned.append(i)
    
    for i in report:
        if i.split()[1] in banned:
            idx = id_list.index(i.split()[0])
            answer[idx] += 1

    return answer