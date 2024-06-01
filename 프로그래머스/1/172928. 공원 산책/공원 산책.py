import copy
def solution(park, routes):
    answer = [0,0]
    x_points = []
    for i, ii in enumerate(park):
        for j in range(len(ii)):
            if ii[j] == "S":
                start_point = [i,j]
            elif ii[j] == "X":
                x_points.append([i,j])

    park = [[j for j in range(len(park[0]))] for i in range(len(park))]
    park[start_point[0]][start_point[1]] = "S"
    for i in x_points:
        park[i[0]][i[1]] = "X"

    for i in routes:
        print(f"i = {i},  start_point = {start_point}")
        op = i.split()[0]
        n = int(i.split()[1])
        roll_back = copy.deepcopy(start_point)
        if op == "E":
            for j in range(n):
                start_point[1] += 1
                if start_point[1] >= len(park[0]) or park[start_point[0]][start_point[1]] == "X":
                    start_point = roll_back
                    break
        elif op == "W":
            for j in range(n):
                start_point[1] -= 1
                if start_point[1] == -1 or park[start_point[0]][start_point[1]] == "X":
                    start_point = roll_back
                    break
        elif op == "S":
            for j in range(n):
                start_point[0] += 1
                if start_point[0] >= len(park) or park[start_point[0]][start_point[1]] == "X":
                    start_point = roll_back
                    break
        elif op == "N":
            for j in range(n):
                start_point[0] -= 1
                if start_point[0] == -1 or park[start_point[0]][start_point[1]] == "X":
                    start_point = roll_back
                    break
    
    return start_point