# 2105. [모의 SW 역량테스트] 디저트 카페

'''
디저트 가게가 모여있는 지역의 한 변의 길이 N과 디저트 카페의 디저트 종류가 입력으로 주어질 때,
임의의 한 카페에서 출발하여 대각선 방향으로 움직이고
서로 다른 디저트를 먹으면서 사각형 모양을 그리며 다시 출발점으로 돌아오는 경우,
디저트를 가장 많이 먹을 수 있는 경로를 찾고, 그 때의 디저트 수를 정답으로 출력하는 프로그램을 작성하라.
만약, 디저트를 먹을 수 없는 경우 -1을 출력한다.
'''

import sys
sys.stdin = open("input.txt", "r")

delta = [(1, -1), (1, 1), (-1, 1), (-1, -1), (1, -1)]    # 델타 생성 (0, 1, 2, 3, 0 방향)


def DFS(n, r, c, v, cnt):                       # DFS 함수 호출 (회전 횟수 n, 출발지 r, c, 디저트 저장하는 v, 갯수 cnt)
    global sr, sc, result                       # global 변수로 출발지와 result 불러 옴
    if n == 2 and result >= cnt*2:              # (가지치기) 방향 n이 2이고 cnt*2의 값이 result보다 같거나 작을 경우는 return
        return

    if n > 3:                                   # n이 3보다 클 경우 4방향을 다 돌았으므로 return
        return

    # 만약 r, c값이 출발지와 일치하고 n 방향이 3이고 cnt의 값이 result 보다 클 경우
    if r == sr and c == sc and n == 3 and result < cnt:
        result = cnt                            # result에 cnt값을 저장후 return
        return

    for k in range(n, n+2):                     # n 방향이 그대로 일때와 하나 이동할 경우를 위해 2번 반복문 실행
        nr = r + delta[k][0]                    # nr에 r + delta[k][0] 의 값을 더하여 저장
        nc = c + delta[k][1]                    # nc에 c + delta[k][1] 의 값을 더하여 저장
        # 만약 nr과 nc가 인덱스 범위 내에 있고 cafe[nr][nc]의 값이 v에 없을 경우
        if 0 <= nr < N and 0 <= nc < N and cafe[nr][nc] not in v:
            v.append(cafe[nr][nc])              # v에 cafe[nr][nc]값을 추가
            DFS(k, nr, nc, v, cnt + 1)          # DFS 함수에 새로운 방향 k와 현재 이동좌표 nr,nc와 v리스트, cnt+1값으로 호출
            v.pop()                             # 함수 return 후 다른 곳을 방문하기 위해 v.pop() 하기


# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())                            # 한 변의 길이 N 입력 받기
    cafe = [list(map(int, input().split())) for _ in range(N)]  # 디저트 종류가 담긴 카페 정보 cafe 리스트로 받기
    result = -1                                 # 결과 값 출력을 위한 result 변수 생성 후 초기값 -1로 설정
    for sr in range(N - 2):                     # 0부터 N-2까지 행 반복 ( 최소 아래로 2줄이 있어야 하기때문)
        for sc in range(1, N - 1):              # 1부터 N-1까지 열 반복 ( 좌우로 최소 1칸이 있어야 하기 때문)
            DFS(0, sr, sc, [], 0)               # DFS 함수 호출 (초기값으로 0번째 방향과, 시작 위치, 디저트 담을 리스트, 디저트 카운트 변수)

    print(f'#{test_case} {result}')             # 결과 출력