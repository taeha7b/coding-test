# 2020.12.01
# https://programmers.co.kr/learn/courses/30/lessons/12903
"""
문제 해결의 아이디어:
글자의 수를 2로 나눈 나머지를 통해서 0일경우 짝수, 0이 아닐경우 홀수로 하여
인덱싱을 통해서 문제를 해결하였다.
"""
def solution(s): 
    div_s = len(s)/2
    answer = 0
    if len(s)%2 == 0:
       	answer = s[int(div_s-1):int(div_s+1)]
    else:
        answer = s[int(div_s-0.5)]
    return answer