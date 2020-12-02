# https://programmers.co.kr/learn/courses/30/lessons/68644
"""
문제 해결의 아이디어:
반복문을 통해서 리스트내의 숫자를 선택합니다. 인덱스와 값을 사용하기 위해서 enumerate를 사용하고,
선택한 숫자와 다른 인덱스의 값들을 차례대로 더해서 빈 배열(answer)에 담습니다.
중복을 제거하기 위해서 set()자료구조를 사용하고, 리스트로 반환합니다.
"""
def solution(numbers):
    answer = []
    for key, value in enumerate(numbers):
        if key == len(numbers)-1:
            pass     
        else:
            for index in range(key+1, len(numbers)):
                answer.append(value + numbers[index])
                
    answer = list(set(answer))
    answer.sort()
    return answer