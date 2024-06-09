def solution(data, ext, val_ext, sort_by):
    answer = []
    dic_ = {"code":0, "date":1, "maximum":2, "remain":3}
    for i in data:
        if i[dic_.get(ext)] < val_ext:
            answer.append(i)
    answer = sorted(answer, key=lambda x:x[dic_.get(sort_by)])
    return answer