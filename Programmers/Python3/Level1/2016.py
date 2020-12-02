# 2020.12.02
# https://programmers.co.kr/learn/courses/30/lessons/12901

# 풀이1
"""
문제 해결의 아이디어:
분명 파이썬이라면 달력에 관한 내장 라이브러리가 있을것이라 확신했기에 문제를 보자마자 라이브러리를 찾았습니다.
(파이썬의 내장라이브러리인 calendar를 사용하여 풀었습니다.)

다만 이렇게 풀려고, 코딩테스트를 하는것은 아니니 라이브러리 사용없이 푸는 풀이2를 추가합니다.
"""
import calendar

def solution(a, b):
    dic = {'0':'MON','1':'TUE','2':'WED','3':'THU','4':'FRI','5':'SAT','6':'SUN'}
    day = str(calendar.weekday(2016, a, b))
    answer = dic[day]
    return answer


# 풀이2
"""
문제 해결의 아이디어:
임의의 월(a), 일(b)에 대해서 각 달의 길이를 더하여 총 길이를 7(일주일)로 나누고
나머지를 이용하여 요일에 매칭하였습니다.
"""
def solution(a, b):
    dic = {'1':'FRI','2':'SAT','3':'SUN','4':'MON','5':'TUE','6':'WED','0':'THU'}
    day_end = {'1':31,'2':29,'3':31,'4':30,'5':31,'6':30,'7':31,'8':31,'9':30,'10':31,'11':30,'12':31}
    day = 0
    for month in range(1,a+1):
        if month != a:
            day += day_end[str(month)]
        else:
            day += b
    
    key = str(day%7)
    answer = dic[key]
    return answer
