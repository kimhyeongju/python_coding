def solution(friends, gifts):
    dic_name = {}
    total = len(friends)
    for i,j in enumerate(friends):
        dic_name[j] = i
    lst_2d = [[0]*total for i in range(total)]
    for i in gifts:
        sender, receiver = i.split(" ")
        s_key, r_key = dic_name.get(sender), dic_name.get(receiver)
        lst_2d[s_key][r_key]  += 1
    
    lst = [0] * total
    for i in range(total):
        for j in range(i+1, total):
            if lst_2d[i][j] > lst_2d[j][i]:
                lst[i] += 1
            elif lst_2d[i][j] < lst_2d[j][i]:
                lst[j] += 1
            else:
                idx_of_i = sum(lst_2d[i]) - sum(k[i] for k in lst_2d)
                idx_of_j = sum(lst_2d[j]) - sum(k[j] for k in lst_2d)
                if idx_of_i > idx_of_j:
                    lst[i] += 1
                elif idx_of_i < idx_of_j:
                    lst[j] += 1
                else:
                    pass

    answer = max(lst)
    return answer