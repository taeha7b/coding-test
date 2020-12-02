# https://programmers.co.kr/learn/courses/30/lessons/64061
"""
문제 해결의 아이디어:
반복문을 사용하여 moves로 받는 리스트를 순회하면서 가장 최상단부터 숫자를 뽑는다.
다음 반복문이 진행될때마다. 가장 끝에있는 숫자[-1]와 그 보다 한칸 앞에 있는 숫자[-2]를 비교하여
같으면 이 둘을 제거한다.  
"""
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