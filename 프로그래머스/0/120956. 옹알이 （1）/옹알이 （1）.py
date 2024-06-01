def solution(babbling):
    answer = 0
    possible = ["aya", "ye", "woo", "ma"]
    for babb in babbling:
        while 1:
            if babb[:3] in ["aya","woo"]:
                babb = babb[3:]
            elif babb[:2] in ["ye", "ma"]:
                babb = babb[2:]
            else:
                break
            if len(babb) == 0:
                answer += 1
                break
    return answer