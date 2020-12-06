# 2020.12.06
# https://programmers.co.kr/learn/courses/30/lessons/12916
"""
문제 해결의 아이디어:
반복문을 사용하여 같은 문제에서 주어진 글자면, 해당 글자를 키로 하는 딕셔너리의 값에 1을 더해주고
조건문을 사용하여 반환값을 결정한다.
"""
def solution(s):
    dic = {'p':0, 'y':0}
    for i in s:
        if i == "p" or i == "P":
            dic['p'] += 1
        elif i == "y" or i == "Y":
            dic['y'] += 1 
    if dic['p'] == dic['y']:
        return True
    elif dic['p'] != dic['y']:
        return False