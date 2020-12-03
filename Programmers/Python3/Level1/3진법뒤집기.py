# 2020.12.04
# https://programmers.co.kr/learn/courses/30/lessons/68935
"""
문제 해결의 아이디어:
10진법으로 주어지는 n을 3진법으로 바꾸고 앞뒤반전을 시키라고 했는데,
이 과정은 반복문을 사용하여 3으로 나눈 나머지를 문자열로 바꿔서 차례대로 더해주면 자연스럽게 처리가 된다.
"""
def solution(n):
    num = n
    temp = ''  
    while True:
        if n < 3:
            return n
        
        val = divmod(num,3)
        if val[0] >= 3:
            num = val[0]
            temp += str(val[1])
        else:
            temp += str(val[1])
            temp += str(val[0])
            break

    reversed_num = str(int(temp))
    sol = 0
    length = len(reversed_num)-1
    for i in reversed_num:
        sol += int(i)*(3**length)
        length -= 1
    return sol