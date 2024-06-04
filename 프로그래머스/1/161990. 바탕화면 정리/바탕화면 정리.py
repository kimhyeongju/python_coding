def solution(wallpaper):
    answer =  []
    lux, luy, rdx, rdy = 0, 0, 0, 0
    arr_items_x = []
    arr_items_y = []
    for idx_i, i in enumerate(wallpaper):
        for idx_j, j in enumerate(i):
            if j == "#":
                arr_items_x.append(idx_i)
                arr_items_y.append(idx_j)
    print(f"arr_x = {arr_items_x}, arr_y = {arr_items_y}")
    lux = min(arr_items_x)
    luy = min(arr_items_y)
    rdx = max(arr_items_x) + 1
    rdy = max(arr_items_y) + 1
    answer = [lux, luy, rdx, rdy]
    return answer