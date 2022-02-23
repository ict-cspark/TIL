# 1220. [S/W 문제해결 기본] 5일차 - Magnetic

'''
테이블 위에 자성체들이 놓여 있다.

자성체들은 성질에 따라 색이 부여되는데, 푸른 자성체의 경우 N극에 이끌리는 성질을 가지고 있고, 붉은 자성체의 경우 S극에 이끌리는 성질이 있다.

아래와 같은 테이블에서 일정 간격을 두고 강한 자기장을 걸었을 때, 시간이 흐른 뒤에 자성체들이 서로 충돌하여 테이블 위에 남아있는 교착 상태의 개수를 구하라.
'''

import sys
sys.stdin = open("input.txt", "r")

# 테스트케이스 입력받기
T = 10

for test_case in range(1, T + 1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for r in range(N):
        isRed = False
        for c in range(N):
            if table[c][r] == 1:
                isRed = True
            elif table[c][r] == 2 and isRed == True:
                result += 1
                isRed = False

    print(f'#{test_case} {result}')
