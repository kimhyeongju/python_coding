def solution(today, terms, privacies):
    answer = []
    today = list(map(int,today.split(".")))
    today = today[0]*336 + today[1]*28 + today[2]

    dic_ = {}
    for i in terms:
        dic_[i.split()[0]] = int(i.split()[1])
    
    cnt = 0
    print(today)
    for i in privacies:
        cnt += 1
        t = dic_.get(i.split()[1]) * 28
        d = i.split()[0]
        d_ = list(map(int, d.split(".")))
        d_ = d_[0]*336 + d_[1]*28 + d_[2] + t
        if d_ <= today:
            answer.append(cnt)
        print(f"cnt = {cnt}, t = {t}, d_ = {d_}")

    return answer