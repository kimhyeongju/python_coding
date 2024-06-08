def solution(board, moves):
    basket = []
    answer = 0
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] == 0:
                pass
            else:
                basket.append(board[j][i-1])
                board[j][i-1] = 0
                break

    n = 0
    while n < len(basket) - 1:
        if basket[n] == basket[n+1]:
            basket.pop(n)
            basket.pop(n)
            answer += 2
            n = 0
        else:
            n += 1


    return answer