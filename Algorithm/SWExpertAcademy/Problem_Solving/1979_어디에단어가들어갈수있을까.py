# 1979. 어디에 단어가 들어갈 수 있을까

'''
N X N 크기의 단어 퍼즐을 만들려고 한다. 입력으로 단어 퍼즐의 모양이 주어진다.

주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램을 작성하라.
'''

import sys
sys.stdin = open("input.txt", "r")

# 퍼즐 체크 함수
def puzzle_check(puzzle):
    length = 0
    result = 0
    # 해당 인덱스에 값이 1일 경우 길이에 1추가
    for r in range(N + 1):
        for c in range(N + 1):
            if puzzle[r][c] == 1:
                length += 1
            # 만약 0일 경우 직전 length 길이가 K와 같을 경우
            # result에 1을 추가하고 length를 0으로 초기화
            else:
                if length == K:
                    result += 1
                    length = 0
                # 아닐 경우 length 만 0으로 초기화
                else:
                    length = 0
    return result

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    # 2차원 행렬 길이 N과 단어 길이 K 입력받기
    N, K = map(int, input().split())

    # 입력값 저장을 위해 리스트 생성
    puzzle = []
    # 우측을 0으로 채운 N+1 x N+1 행렬을 만들기 위해 input 값 끝에 0을 추가
    for _ in range(N):
        words = input() + ' 0'
        puzzle += [list(map(int, words.split()))]
    # 하단에 0으로 채운 리스트 한줄을 추가
    puzzle += [[0] * (N + 1)]
    # 열기준 탐색을 위해 zip함수 이용
    puzzle_c = list(map(list, zip(*puzzle)))

    # puzle_check 함수에 행기준과 열기준을 탐색 후 결과값에 저장 후 출력
    result = puzzle_check(puzzle) + puzzle_check(puzzle_c)
    print(f'#{test_case} {result}')
