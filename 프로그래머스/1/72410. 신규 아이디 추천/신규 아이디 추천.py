def solution(new_id):
    answer = step1(new_id)
    answer = step2(answer)
    answer = step3(answer)
    answer = step4(answer)
    answer = step5(answer)
    answer = step6(answer)
    answer = step7(answer)
    return answer

def step1(new_id):
    return new_id.lower()

def step2(new_id):
    copied_id = new_id
    allows = '0123456789abcdefghijklmnopqrstuvwxyz-_.'
    for i in new_id:
        if i not in allows:
            copied_id = copied_id.replace(i,'')
    return copied_id

def step3(new_id):
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    return new_id

def step4(new_id):
    if new_id == ".":
        return "aaa"
    else:
        if new_id[0] == ".":
            new_id = new_id[1:]
        if new_id[-1] == ".":
            new_id = new_id[:-1]
        return new_id

def step5(new_id):
    if new_id == '':
        new_id = 'aaa'
    return new_id

def step6(new_id):
    if len(new_id) >= 16:
        new_id = new_id[:15]
    while new_id[-1] == ".":
        new_id = new_id[:-1]
    return new_id

def step7(new_id):
    if len(new_id) <= 2:
        while len(new_id) <= 2:
            new_id = new_id + new_id[-1]
    return new_id