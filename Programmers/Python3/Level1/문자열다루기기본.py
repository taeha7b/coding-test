# 2020.12.07
# https://programmers.co.kr/learn/courses/30/lessons/12918
"""
문제 해결의 아이디어:
문자열로 "0123" 이렇게 s가 구성될수 있기에 int로 변환을 해주고, 그 값의 길이를 확인하여 적절한 반환값을 넘겨주었습니다.
만약에 s가 "a123"과 같이 문자가 섞인 값으로 구성되면 int로 형변환할때 오류를 발생시키기에  try, except 를 사용하여 처리했습니다.

새롭게 안것들: 
isalpha함수: 문자열이 문자로 구성되어 있는지 아닌지를 확인하여 True 또는 False로 반환합니다.
isdigit함수: 문자열이 숫자로 구성되어 있는지 아닌지를 확인하여 True 또는 False로 반환힙니다.
"""
def solution(s):
    try:
        convert_s = int(s)
        if len(str(convert_s)) == 4 or len(str(convert_s)) == 6:
            return True
        else:
            return False
    except Exception:
        return False