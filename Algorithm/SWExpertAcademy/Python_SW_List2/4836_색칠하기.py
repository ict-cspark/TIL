# 4836. [파이썬 S/W 문제해결 기본] 2일차 - 색칠하기 

'''
그림과 같이 인덱스가 있는 10x10 격자에 빨간색과 파란색을 칠하려고 한다.

N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때, 칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하는 프로그램을 만드시오.

주어진 정보에서 같은 색인 영역은 겹치지 않는다.
'''

import sys
sys.stdin = open('input.txt', 'r')

# 테스트 케이스 입력
T = int(input())

for t in range(1, T+1):
    # 칠할 영역 개수 N 입력받기
    N = int(input())

    # 10x10 격자를 이중리스트를 이용해 0으로 채우기
    coor = [[0]*10 for _ in range(10)]

    # 인덱스와 색상 정보를 N 개수만큼 받기
    for n in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        # r1, r2와 c1, c2의 값을 이용하여 coor에 접근하여 색상에 따라 값을 달리 추가
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                if color == 1:
                    coor[r][c] += 1
                else:
                    coor[r][c] += 100

    # 결과값 저장을 위한 result 변수 생성 후 coor 리스트를 순차탐색
    result = 0
    for i in range(10):
        for j in range(10):
            # coor의 요소가 100보다 크고 100으로 나눈 나머지가 존재할 경우
            if coor[i][j] > 100 and coor[i][j] % 100 > 0:
                # result에 +1
                result += 1

    print(f'#{t} {result}')

