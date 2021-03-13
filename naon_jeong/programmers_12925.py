'''
프로그래머스 코딩테스트 연습 - 문자열을 정수로 바꾸기
https://programmers.co.kr/learn/courses/30/lessons/12925

문자열 s를 숫자로 변환한 결과를 반환하는 함수, solution을 완성하세요.

- s의 길이는 1 이상 5이하입니다.
- s의 맨앞에는 부호(+, -)가 올 수 있습니다.
- s는 부호와 숫자로만 이루어져있습니다.
- s는 "0"으로 시작하지 않습니다.

예를들어 str이 "1234"이면 1234를 반환하고, "-1234"이면 -1234를 반환하면 됩니다.
str은 부호(+,-)와 숫자로만 구성되어 있고, 잘못된 값이 입력되는 경우는 없습니다.
'''

def solution(s):
    answer = 0
    if '+' in s:
        s = s[1:]
    elif '-' in s:
        s = s[1:]
        answer = int(s) * -1
        return answer
    answer = int(s)
    return answer


# 부호 상관 없이 타입 변경이 된다는 것을 알았다
def solution2(s):
    return int(s)
