# 2819. 격자판의 숫자 이어 붙이기

'''
4×4 크기의 격자판이 있다. 격자판의 각 격자칸에는 0부터 9 사이의 숫자가 적혀 있다.
격자판의 임의의 위치에서 시작해서, 동서남북 네 방향으로 인접한 격자로 총 여섯 번 이동하면서,
각 칸에 적혀있는 숫자를 차례대로 이어 붙이면 7자리의 수가 된다.
이동을 할 때에는 한 번 거쳤던 격자칸을 다시 거쳐도 되며, 0으로 시작하는 0102001과 같은 수를 만들 수도 있다.
단, 격자판을 벗어나는 이동은 가능하지 않다고 가정한다.
격자판이 주어졌을 때, 만들 수 있는 서로 다른 일곱 자리 수들의 개수를 구하는 프로그램을 작성하시오.
'''

import sys
sys.stdin = open("input.txt", "r")


delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]          # 델타 리스트 생성 (상, 우, 하, 좌)

def DFS(n, r, c, num):                              # DFS 함수로 인자는 횟수 n, 가로 r, 세로 c, 최종 숫자 num
    if n == 7:                                      # n이 7일 경우 result에 num값을 추가하고 리턴
        result.add(num)
        return

    for dr, dc in delta:                            # 델타만큼 반복문 실행
        nr = r + dr                                 # nr에 r + dr 값을 저장
        nc = c + dc                                 # nc에 c + dc 값을 저장
        if 0 <= nr < 4 and 0 <= nc < 4:             # 만약 nr과 nc가 인덱스 범위 내에 있을 경우
            DFS(n+1, nr, nc, num*10 + arr[nr][nc])  # n에 1을 더하고, nr, nc 값과 num값에 기존 num값 * 10 + arr[nr][nc]의 값으로 호출


# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    result = set()                                  # 중복값을 방지하기 위해 set형식의 result 생성

    for r in range(4):                              # 4 x 4 arr 배열을 하나씩 DFS 함수로 호출
        for c in range(4):
            DFS(0, r, c, 0)

    print(f'#{test_case} {len(result)}')            # result의 길이를 출력