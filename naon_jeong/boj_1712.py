'''
백준 온라인 저지 - 손익분기점

https://www.acmicpc.net/problem/1712

월드전자는 노트북을 제조하고 판매하는 회사이다.
노트북 판매 대수에 상관없이 매년 임대료, 재산세, 보험료, 급여 등 A만원의 고정 비용이 들며,
한 대의 노트북을 생산하는 데에는 재료비와 인건비 등 총 B만원의 가변 비용이 든다고 한다.

노트북 가격이 C만원으로 책정되었다고 한다.
일반적으로 생산 대수를 늘려 가다 보면 어느 순간 총 수입(판매비용)이 총 비용(=고정비용+가변비용)보다 많아지게 된다.
최초로 총 수입이 총 비용보다 많아져 이익이 발생하는 지점을 손익분기점(BREAK-EVEN POINT)이라고 한다.

A, B, C가 주어졌을 때, 손익분기점을 구하는 프로그램을 작성하시오.
'''


'''
노트북 가격 * 생산 대수 > (고정 비용 + 가변 비용 * 생산 대수)
인 지점을 찾아 생산 대수를 출력하는 문제다.
따라서, 생산 대수 > 고정 비용 / (노트북 가격 - 가변 비용), 즉 x > A / (C - B) 인 자연수 x를 찾으면 된다.
A / (C - B)가 소수점일 수 있으니 floor 함수를 이용해 소수점 이하는 버림한 뒤 1을 더한다.
만약 (노트북 가격 - 가변 비용이) 음수거나 0이면 -1을 출력한다.
'''

import math
A, B, C = list(map(int, input().split()))

if (C - B) <= 0:
    print(-1)
else:
    result = math.floor(A / (C - B)) + 1
    print(result)
