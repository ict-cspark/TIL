# Baekjoon Online Judge - 체스판 다시 칠하기

'''
보드가 체스판처럼 칠해져 있다는 보장이 없어서,
지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다.
당연히 8*8 크기는 아무데서나 골라도 된다.
지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.
'''


N, M = map(int, input().split())
board = [list(map(str, input())) for _ in range(N)]     # 체스판 입력 받기

WC = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']           # 백으로 시작하는 체스판 구성
BC = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']           # 흑으로 시작하는 체스판 구성


def check(sr, sc, flag):                                # 규칙성 없는 돌을 찾기 위한 check 함수
    global count                                        # count를 global 변수로 호출

    answer = 0                                          # answer 0으로 초기화
    for r in range(sr, 8 + sr):                         # r은 sr부터 8 + sr 범위만큼 반복문 실행
        row = board[r][sc:8 + sc]                       # row에 board[r][sc:8 + sc] 슬라이싱 하여 저장
        if flag:                                        # flag가 True라면 compare에 BC 리스트 저장
            compare = BC
        else:
            compare = WC                                # False일 경우 compare에 WC 리스트 저장
        for c in range(8):                              # 한 행 크기인 8만큼 반복문 실행
            if row[c] != compare[c]:                    # row[c]와 compare[c]가 같지 않다면
                answer += 1                             # answer에 1을 더함

        flag = not flag                                 # flag 전환

    if count > answer:                                  # 만약 count보다 answer가 작다면
        count = answer                                  # count값 answer로 갱신
    return


count = 999                                             # 최솟값을 찾기 위한 count 변수 생성
for i in range(N - 7):                                  # N-7, M-7 범위 만큼 반복문 실행
    for j in range(M - 7):
        check(i, j, False)                              # check 함수에 i, j, False 값으로 호출
        check(i, j, True)                               # check 함수에 i, j, True 값으로 호출

print(count)                                            # count 값 출력