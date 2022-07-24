# Baekjoon Online Judge - 봄버맨

'''
폭탄을 설치해놓은 초기 상태가 주어졌을 때, N초가 흐른 후의 격자판 상태를 구하려고 한다.
'''

import sys
input = sys.stdin.readline

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]          # 델타를 위한 리스트 생성

R, C, N = map(int, input().split())                 # R, C, N 입력받기

board = [list(map(str, input().strip())) for _ in range(R)] # 격자판 입력 받기

if N <= 1:                                          # N이 1보다 작을 경우 그대로 출력
    for res in board:
        print("".join(res))

elif N%2 == 0:                                      # N이 짝수일 경우 폭탄 모두 채워 출력
    for _ in range(R):
        print('O' * C)

else:
    board_bomb1 = [['O'] * C for _ in range(R)]     # 초기 설치한 폭탄이 터진 격자판 출력
    for r in range(R):
        for c in range(C):
            if board[r][c] == 'O':                  # 폭탄이 있을 경우
                board_bomb1[r][c] = '.'             # 해당 위치 폭탄 터트린 후
                for dr, dc in delta:                # 델타 4방향 탐색하여
                    nr = dr + r
                    nc = dc + c
                    if 0 <= nr < R and 0 <= nc < C:
                        board_bomb1[nr][nc] = '.'   # 폭탄 터트림

    board_bomb2 = [['O'] * C for _ in range(R)]     # 두번째로 설치한 폭탄이 터진 격자판 출력
    for r in range(R):
        for c in range(C):                          # 하지만 초기 설치한 폭탄으로 인해 없어진 폭탄은 미반영
            if board_bomb1[r][c] == 'O':            # 폭탄이 있을 경우 해당 폭탄 터트린 후 
                board_bomb2[r][c] = '.'
                for dr, dc in delta:                # 델타 4방향 탐색하여
                    nr = dr + r
                    nc = dc + c
                    if 0 <= nr < R and 0 <= nc < C:
                        board_bomb2[nr][nc] = '.'   # 폭탄 터뜨림

    if N%4 == 3:                                    # N을 4로 나눈 나머지가 3일 경우 초기 폭탄 출력
        for res in board_bomb1:
            print("".join(res))
    elif N%4 == 1:                                  # N을 4로 나는 나머지가 1일 경우 두번째 설치 폭탄 출력
        for res in board_bomb2:
            print("".join(res))
