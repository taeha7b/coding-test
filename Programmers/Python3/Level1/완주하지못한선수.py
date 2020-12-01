# https://programmers.co.kr/learn/courses/30/lessons/42576

import collections

def solution(participant, completion):
    participant = collections.Counter(participant)
    completion = collections.Counter(completion)
    player = list((participant - completion).keys())[0]
    return player