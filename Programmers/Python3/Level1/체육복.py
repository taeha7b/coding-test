# https://programmers.co.kr/learn/courses/30/lessons/42862
"""
문제 해결의 아이디어:
체육복을 잃어버린 학생이 체육복을 가져왔을경우 본인이 입어야 하기에 빌려줄수 없다.
따라서 lost로 받는 리스트와 reserve로 받는 리스트에 같은 숫자(학생)가 있는지 확인하여 제거하고
lost로 받는 리스트에 있는 학생을 반복문으로 순회하면서 reserve로 받는 리스트내에 1작은 숫자가 있는지 확인하고
없으면 1큰 숫자가 있는지 확인하면서 최대값(n)을 구한다.
"""
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