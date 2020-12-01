# https://programmers.co.kr/learn/courses/30/lessons/68644

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