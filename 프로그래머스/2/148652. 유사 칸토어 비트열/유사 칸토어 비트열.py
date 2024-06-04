def solution(n, l, r):
    answer = 0
    ones = 0
    l = ones_cnt(n,l-1,ones)
    r = ones_cnt(n,r,ones)
    answer = r-l
    return answer

def ones_cnt(n,x, ones):
    if n == 1:
        temp = [i for i in range(x) if i != 2]
        ones += len(temp)
        return ones
    remainder_x = x % 5**(n-1)
    x = x // 5**(n-1)
    if x > 0:
        temp = [i for i in range(x) if i != 2]
        ones += len(temp) * 4**(n-1)
    if x == 2:
        return ones
    ones = ones_cnt(n-1, remainder_x, ones)
    return ones