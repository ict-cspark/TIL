# 3499. 퍼펙트 셔플

'''
카드를 퍼펙트 셔플 한다는 것은, 카드 덱을 정확히 절반으로 나누고 나눈 것들에서 교대로 카드를 뽑아 새로운 덱을 만드는 것을 의미한다.
N개의 카드가 있는 덱이 주어질 때 이를 퍼펙트 셔플하면 어떤 순서가 되는지 출력하는 프로그램을 작성하라.
'''

import sys

sys.stdin = open("input.txt", "r")

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    words = list(map(str, input().split()))

    center = (N+1)//2   # center에 중간값을 대입

    result = ''         # 결과값 저장을 위한 result 변수 생성
    for i in range(center):
        result += words[i] + ' '    # result에 word[i]추가
        if center + i < N:          # 만약 center + i 가 N 이내일 경우
            result += words[center + i] + ' '   # result에 word[center + i] 추가 (중간 이후)

    print(f'#{test_case} {result}') # 결과값 출력