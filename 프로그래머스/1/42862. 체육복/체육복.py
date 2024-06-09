def solution(n, lost, reserve):
    arr = [1] * n
    for i in lost:
        arr[i-1] = arr[i-1] - 1
    for i in reserve:
        arr[i-1] = arr[i-1] + 1



    if arr[0] == 0 and arr[1] == 2:
        arr[0] = 1
        arr[1] = 1
    if arr[n-1] == 0 and arr[n-2] == 2:
        arr[n-1] = 1
        arr[n-2] = 1

    for i in range(n):
        if i >= 1 and i <= n-2:
            if arr[i] == 0:
                if arr[i-1] == 2:
                    arr[i] = 1
                    arr[i-1] = 1
                elif arr[i+1] == 2:
                    arr[i] = 1
                    arr[i+1] = 1


    return n - arr.count(0)