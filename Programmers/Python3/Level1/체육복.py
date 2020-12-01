# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    n -= len(lost)
    dupl=[i for i in lost if i in reserve]
    n+=len(dupl)
    for lost_num in dupl:
        reserve.remove(lost_num)
        lost.remove(lost_num)
    
    for lost_num in lost:
        if lost_num-1 in reserve:
            reserve.remove(lost_num-1)
            n+=1
        elif lost_num+1 in reserve:
            reserve.remove(lost_num+1)
            n+=1
    return n