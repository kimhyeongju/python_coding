from collections import deque
def solution(land):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    rows = len(land)
    columns = len(land[0])
    visited = [[False]*columns for _ in range(rows)]
    visited_dic = dict()
    visited_dic[False] = 0

    def bfs(k, row, col):
        cnt = 1
        temp = []
        visited[row][col] = True
        queue = deque()
        queue.append((row, col))
        while queue:
            cur_x, cur_y = queue.popleft()
            temp.append((cur_x, cur_y))
            for i in range(4):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]
                if 0 <= next_x < rows and 0 <= next_y < columns:
                    if land[next_x][next_y] == 1 and not visited[next_x][next_y]:
                        queue.append((next_x, next_y))
                        visited[next_x][next_y] = True
                        cnt += 1
        for i, j in temp:
            visited[i][j] = k
        visited_dic[k] = cnt
    
    k=1
    for row in range(rows):
        for col in range(columns):
            if land[row][col] == 1 and not visited[row][col]:
                bfs(k, row, col)
                k += 1
    
    visited_set = [set(x) for x in zip(*visited)]
    ans_list = []
    for temp in visited_set:
        res = 0
        for i in temp:
            res += visited_dic.get(i)
        ans_list.append(res)
        
    return max(ans_list)