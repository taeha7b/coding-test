# 2020.12.06
# https://programmers.co.kr/learn/courses/30/lessons/12910
"""
문제 해결의 아이디어:
나누어 떨어지면 나머지가 0인것을 활용하여 문제를 해결한다.
"""
def solution(arr, divisor):
    answer = []
    if divisor == 1:
        arr.sort()
        return arr
    for i in arr:
        if i%divisor == 0:
            answer.append(i)
    if len(answer) == 0:
        answer.append(-1)   
    answer.sort()
    return answer