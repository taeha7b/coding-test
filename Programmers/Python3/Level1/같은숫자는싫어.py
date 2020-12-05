# 2020.12.05
# https://programmers.co.kr/learn/courses/30/lessons/12906
"""
문제 해결의 아이디어:
문제에서 주어진 리스트(arr)에서 첫번째 값을 리스트(answer)에 넣고, 
반복문을 통해서 리스트(arr)의 2번째 값부터 이전 인덱스의 값과 같은지 확인하여
같지 않을 경우에만 리스트(answer)에 추가하여 반환했습니다.
"""
def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])

    return answer