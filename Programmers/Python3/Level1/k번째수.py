# https://programmers.co.kr/learn/courses/30/lessons/42748
"""
문제 해결의 아이디어:

"""
def solution(array, commands):
    answer = []
    for data_list in commands:
        pick = array[data_list[0]-1:data_list[1]]
        pick.sort()
        answer.append(pick[data_list[2]-1])
    
    return answer