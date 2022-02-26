# 1974. 스도쿠 검증

'''
입력으로 9 X 9 크기의 스도쿠 퍼즐의 숫자들이 주어졌을 때, 위와 같이 겹치는 숫자가 없을 경우, 1을 정답으로 출력하고 그렇지 않을 경우 0 을 출력한다.
'''

import sys
sys.stdin = open("input.txt", "r")

# Set을 이용하여 9개의 입력을 받아 길이가 9일 경우에만 True값을 리턴
def check(puzzle):
    for r in range(9):
        ck = set()
        for c in range(9):
            ck.add(puzzle[r][c])
        if len(ck) != 9:
            return False
    return True

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    # 9줄을 입력받아 2차원 리스트로 저장
    puzzle = []
    for n in range(9):
        puzzle += [list(map(int, input().split()))]

    # 열방향 검증을 위해 zip함수 이용
    puzzle_c = list(map(list, zip(*puzzle)))
    # 3x3 검증을 위해 3행 3열씩 반복하여 리스트에 저장
    puzzle_9 = []
    for i in range(3):
        for j in range(3):
            puzzle_3 = []
            for rr in range((3*j), (3*(j+1))):
                for cc in range((3*i), (3*(i+1))):
                    puzzle_3.append(puzzle[rr][cc])
            puzzle_9 += [puzzle_3]

    # 만약 세가지 경우 모두 True일 경우에만 result에 1을 추가
    if check(puzzle) and check(puzzle_c) and check(puzzle_9):
        result = 1
    else:
        result = 0

    # 결과값 출력
    print(f'#{test_case} {result}')


# 2번째 방법
'''
import sys
sys.stdin = open("input.txt", "r")

def check(ARR):
    for r in range(9):
        cnt = [0] * 10
        for c in range(9):
            t = ARR[r][c]
            if cnt[t] == 1:
                return 0
            else:
                cnt[t] = 1
    return 1

def check3(ARR):
    for stR in range(0, 9, 3):
        for stC in range(0, 9, 3):
            cnt = [0] * 10
            for r in range(3):
                for c in range(3):
                    t = ARR[stR+r][stC+c]
                    if cnt[t] == 1:
                        return 0
                    else:
                        cnt[t] = 1
    return 1

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    ARR = [list(map(int, input().split())) for _ in range(9)]
    ARR_C = list(map(list, zip(*ARR)))


    result1 = check(ARR)
    result2 = check(ARR_C)
    result3 = check3(ARR)

    if result1 == 0 or result2 == 0 or result3 == 0:
        result = 0
    else:
        result = 1

    print(f'#{test_case} {result}')
'''