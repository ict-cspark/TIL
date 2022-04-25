# Baekjoon Online Judge - 체스판 다시 칠하기

'''
보드가 체스판처럼 칠해져 있다는 보장이 없어서,
지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다.
당연히 8*8 크기는 아무데서나 골라도 된다.
지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.
'''


N, M = map(int, input().split())
board = [list(map(str, input())) for _ in range(N)]

WC = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
BC = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']


def check(sr, sc, flag):
    global count

    answer = 0
    for r in range(sr, 8 + sr):
        row = board[r][sc:8 + sc]
        if flag:
            compare = BC
        else:
            compare = WC
        for c in range(8):
            if row[c] != compare[c]:
                answer += 1

        flag = not flag

    if count > answer:
        count = answer
    return


count = 999
for i in range(N - 7):
    for j in range(M - 7):
        check(i, j, False)
        check(i, j, True)

print(count)