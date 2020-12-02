# https://programmers.co.kr/learn/courses/30/lessons/42748
"""
문제 해결의 아이디어:
리스트는 순회가 가능한 자료구조이며, 리스트 안에 리스트를 넣어서도 순회가 가능함
commands로 리스트를 받고, 내부의 리스트를 선택하여 인덱싱을 통해서 숫자를 선택합니다.
"""
def solution(array, commands):
    answer = []
    for data_list in commands:
        pick = array[data_list[0]-1:data_list[1]]
        pick.sort()
        answer.append(pick[data_list[2]-1])
    
    return answer