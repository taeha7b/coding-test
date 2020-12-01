def solution(board, moves):
    answer = 0
    temp =[]
    for move in moves:
        for row in board:
            if row[move-1] != 0:
                temp.append(row[move-1])
                row[move-1]=0
                if len(temp) >=2 and temp[-2] == temp[-1]:
                    temp.pop()
                    temp.pop()
                    answer += 2
                break 
    return answer