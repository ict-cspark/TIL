# 5356. 의석이의 세로로 말해요

'''
칠판에 붙여진 단어들이 주어질 때, 의석이가 세로로 읽은 순서대로 글자들을 출력하는 프로그램을 작성하라.
'''

import sys
sys.stdin = open("input.txt", "r")

# 테스트케이스 입력받기
T = int(input())


for test_case in range(1, T + 1):
    # 다섯 줄의 단어를 입력 받고 2차원 행렬로 바꾸기
    words = []
    for _ in range(5):
        words += [list(map(str, input()))]

    # 결과값 저장을 위한 result 변수 생성
    result = ''
    # 열 탐색으로 반복문 실행 (열 15, 행 5)
    for c in range(15):
        for r in range(5):
            # 만약 행의 길이가 현재 열의 길이보다 클 경우에만 조건문 실행
            if len(words[r]) > c:
                # result에 해당 글자 추가
                result += words[r][c]
            # 아닐경우 다음 반복문 실행
            else:
                continue
    # 결과값 저장
    print(f'#{test_case} {result}')
