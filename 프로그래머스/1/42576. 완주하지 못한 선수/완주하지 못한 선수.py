def solution(participant, completion):
    participant.sort()
    completion.sort()
    completion.append(None)

    n = 0
    while participant[n] == completion[n]:
        n += 1

    return participant[n]