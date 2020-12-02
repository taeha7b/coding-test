# 2020.12.01
# https://programmers.co.kr/learn/courses/30/lessons/42840
"""
문제 해결의 아이디어:
모의고사의 문제 번호를 1번학생(a), 2번학생(b), 3번학생(c)의 답안의 수로 나눈
나머지를 찾고, 이 나머지가 세 학생의 연속적인 답안의 인덱스에 해당한다는것을 생각하여 해결했다.
"""
def solution(answers):
    answer = {'1':0, '2':0, '3':0}
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5,]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5,]
    
    for idx, val in enumerate(answers):
        a_check = idx % len(a)
        b_check = idx % len(b)
        c_check = idx % len(c)
        
        if val == a[a_check]:
            answer['1'] += 1
        if val == b[b_check]:
            answer['2'] += 1      
        if val == c[c_check]:
            answer['3'] += 1
                
    max_val = max(answer.values())
    sol = []
    for i in answer:
        if answer[i] == max_val:
            sol.append(int(i))

    sol.sort()
    return sol