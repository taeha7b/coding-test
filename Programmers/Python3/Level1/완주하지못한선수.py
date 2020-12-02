# https://programmers.co.kr/learn/courses/30/lessons/42576
"""
문제 해결의 아이디어:
내장 라이브러리 collections을 사용하여 풀었습니다.
"""
import collections

def solution(participant, completion):
    participant = collections.Counter(participant)
    completion = collections.Counter(completion)
    player = list((participant - completion).keys())[0]
    return player