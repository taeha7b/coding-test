# 2020.12.06
# https://programmers.co.kr/learn/courses/30/lessons/12912
"""
문제 해결의 아이디어:
sum과 range를 활용하여 문제를 푼다.
"""
def solution(a, b):
    if b>a:
        answer = sum(range(a,b+1))
    else:
        answer = sum(range(b,a+1))
    return answer