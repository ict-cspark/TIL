# 4615. 재미있는 오셀로 게임

'''
보드에 빈 곳이 없거나 양 플레이어 모두 돌을 놓을 곳이 없으면 게임이 끝나고 그 때 보드에 있는 돌의 개수가 많은 플레이어가 승리하게 된다.
'''

import sys
sys.stdin = open("input.txt", "r")

# 델타 생성 ( 상, 하, 좌, 우, 좌상, 우상, 우하, 좌하)
delta = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, 1), (1, -1)]


def game(sr, sc, color):                                            # game 함수 (인자값으로 시작 위치와 돌 색상)
    board[sr][sc] = color                                           # board[sr][sc] 에 색깔 정보와 일치하는 돌 저장

    for dr, dc in delta:                                            # 델타 길이만큼 반복
        temp = []                                                   # 돌 색깔을 바꾸기 위한 임시 저장 리스트 생성
        for n in range(1, N):                                       # 1부터 N - 1 까지 반복
            nr = sr + (dr * n)                                      # nr에 sr + (dr * n) 값 저장
            nc = sc + (dc * n)                                      # nc에 sc + (dc * n) 값 저장
            # 만약 nr과 nc가 인덱스 범위 내이고 해당 위치에 돌이 있으며 돌 색깔이 다르다면
            if 0 < nr <= N and 0 < nc <= N and board[nr][nc] != 0 and board[nr][nc] != board[sr][sc]:
                temp.append([nr, nc])                               # 해당 인덱스 정보를 temp에 추가
            # 만약 인덱스 범위 내이고 돌 색깔이 같다면
            elif 0 < nr <= N and 0 < nc <= N and board[nr][nc] == board[sr][sc]:
                for r, c in temp:                                   # temp 리스트 길이만큼 반복
                    if color == 1:                                  # 처음 넣은 돌이 흑돌이라면
                        board[r][c] = 1                             # temp의 돌을 모두 흑돌로 변경
                    else:                                           # 처음 넣은 돌이 백돌이라면
                        board[r][c] = 2                             # temp의 돌을 모두 백돌로 변경
                break                                               # temp의 모든 돌을 바꿨을 경우 반복문 종료 후 다음 델타방향 시작
            else:                                                   # 해당 위치에 돌이 없을 경우
                break                                               # 다음 델타방향 시작
    return


# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):

    N, M = map(int, input().split())                                # 판 크기 N과 플레이 횟수 M 입력 받기
    play = [list(map(int, input().split())) for _ in range(M)]      # play 정보 입력 받아 리스트에 저장

    board = [[0] * (N + 1) for _ in range(N + 1)]                   # 인덱스를 맞추기 위해 N+1 * N+1 오셀로판 생성
    board[N//2][N//2], board[(N//2) + 1][(N//2) + 1] = 2, 2         # 초기 말 위치에 흑돌 저장
    board[N//2][(N//2) + 1], board[(N//2) + 1][N//2] = 1, 1         # 초기 말 위치에 백돌 저장

    for sr, sc, color in play:                                      # play 리스트 길이만큼 반복하여 game 함수 호출
        game(sr, sc, color)                                         # 인자값 말 위치와 색깔 정보

    black = 0                                                       # 갯수를 구하기 위해 black 과 white 변수 생성
    white = 0
    for i in range(N + 1):                                          # N + 1 행 길이만 큼 반복
        black += board[i].count(1)                                  # 해당 행에 흑돌 갯수 black에 저장
        white += board[i].count(2)                                  # 해당 행에 백돌 갯수 white에 저장

    print(f'#{test_case} {black} {white}')                          # 결과값 출력