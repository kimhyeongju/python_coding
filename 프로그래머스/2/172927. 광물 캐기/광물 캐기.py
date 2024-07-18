def myfunc(lst):
    temp = 0
    for l in lst:
        if l == 'diamond':
            temp += 25
        elif l == 'iron':
            temp += 5
        else:
            temp += 1
    return temp


def solution(picks, minerals):
    dia, iron, stone = picks
    length = len(minerals)
    num = dia + iron + stone
    if length//5 +1 > num:
        minerals = minerals[:num*5]
    ans = 0
    mylist = []
    for _ in range(length//5 + 1):
        if len(minerals) == 0:
            break
        elif len(minerals) >= 5:
            mylist.append(minerals[:5])
            minerals = minerals[5:]
        else:
            mylist.append(minerals[:])
            break

    value_list = list(map(myfunc, mylist))
    mydict = dict()
    for i, v in enumerate(value_list):
        mydict[v] = mylist[i]
    value_list = sorted(value_list, reverse=True)

    for v in value_list:
        if dia > 0:
            dia -= 1
            ans += len(mydict[v])
        elif iron > 0:
            iron -= 1
            for i in mydict[v]:
                if i == 'diamond':
                    ans += 5
                else:
                    ans += 1
        elif stone > 0:
            stone -= 1
            for i in mydict[v]:
                if i == 'diamond':
                    ans += 25
                elif i == 'iron':
                    ans += 5
                else:
                    ans += 1
        else:
            return ans
    return ans