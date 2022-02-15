# 1210. [S/W 문제해결 기본] 2일차 - Ladder1

'''
점심 시간에 산책을 다니는 사원들은 최근 날씨가 더워져, 사다리 게임을 통하여 누가 아이스크림을 구입할지 결정하기로 한다.
김 대리는 사다리타기에 참여하지 않는 대신 사다리를 그리기로 하였다.
사다리를 다 그리고 보니 김 대리는 어느 사다리를 고르면 X표시에 도착하게 되는지 궁금해졌다. 이를 구해보자
'''

import sys
sys.stdin = open('input.txt', 'r')

# 테스트 케이스 입력 받기 (10)
T = 10

for t in range(1, T+1):
    N = int(input())
    # 100x100 2차원 배열 입력받아 data 2차원 배열 생성
    data = []
    for n in range(100):
        data += [list(map(int, input().split()))]

    # 좌, 우, 위로 구성된 델타 배열 생성
    dr = [0, 0, -1]
    dc = [-1, 1, 0]

    # 역으로 올라가기 위해 마지막줄에서 2를 찾기
    nc = 0
    for i in range(100):
        if data[99][i] == 2:
            nc = i
            break

    # 마지막줄부터 출발해서 역으로 올라가면서 찾아보기
    nr = 99
    # 첫째줄에 도착하면 반복문 종료
    while nr != 0:
        # 좌, 우, 위 방향으로 반복
        for d in range(3):
            # 올바른 방향이 아닐경우 초기화를 위해 새로운 변수 사용
            new_nr = nr + dr[d]
            new_nc = nc + dc[d]
            # 만약 new_nr과 new_nc가 범위안에 있고 data[new_nr][new_nc] 값이 1일 경우
            while 0 <= new_nr < 100 and 0 <= new_nc < 100 and 0 < data[new_nr][new_nc] < 2:
                # 이동한 곳은 값을 표시하기 위해 2로 변경
                data[new_nr][new_nc] = 2
                # nr과 nc 값을 이동한 방향 좌표의 값 만큼 더함
                nr += dr[d]
                nc += dc[d]

    # 종료했을 때의 nc값을 출력
    print(f'#{t} {nc}')