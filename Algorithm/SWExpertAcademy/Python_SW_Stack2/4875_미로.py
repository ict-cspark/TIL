import sys
sys.stdin = open("input.txt", "r")

dr = [0, 0, -1, 1] # 델타 4방향 생성
dc = [-1, 1, 0, 0] # 상, 하, 좌, 우

def mazecheck(maze):        # 미로 출구있는지 확인하는 함수
    stack = [(sr, sc)]      # stack의 초기값을 sr, sc값을 튜플형태로 저장
                            # 스택이 비어있지 않을 경우 계속 반복문 실행
    while stack != []:      # 스택이 비어있을 경우는 모든 경로를 다갔지만 출구를 못 찾았을 경우
        r, c = stack.pop()  # 스택의 요소를 꺼내와 r과 c에 각각 저장
        maze[r][c] = 1      # 지나간 요소는 1로 변경
        for d in range(4):  # 델타 요소만큼 반복문 실행
            nr = r + dr[d]  # 새로운 위치 값으로 기존위치에 델타 인덱스 요소 더함
            nc = c + dc[d]
            if rangecheck(nr, nc):  # rangecheck 함수를 불러와서 True일 경우는 인덱스 요소 벗어났으므로 다음 반복문 실행
                continue
            elif maze[nr][nc] == 3: # 이동한 위치가 3일 경우 return 1을 하고 종료
                return 1
            elif maze[nr][nc] == 0: # 이동한 위치가 0일 경우 stack에 위치 저장
                stack.append((nr, nc))
    return 0                        # 만약 막다른길에 도착했을 경우 스택에 저장된 요소가 있을 경우
                                    # 해당 지점으로 이동하고 스택이 비어있을 경우 while문을 빠져나와 0을 return
def rangecheck(nr, nc):     # 범위 체크 함수
    if nr < 0 or nc < 0 or nr >= N or nc >= N:  # 만약 nr과 nc중에 하나라도 0보다 작거나 N과 같거나 크다면
        return True                             # True를 return 하여 델타 반복문에서 continue 할수 있게 함
    return False                                # False일 경우 다음 조건문 실행 할 수 있게 함

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]      # 2차원 리스트 maze 생성

    for i in range(N):                                      # 2의 위치를 찾아 sr, sc에 각각 저장
        for j in range(N):
            if maze[i][j] == 2:
                sr, sc = i, j
                break

    result = mazecheck(maze)                                # mazecheck 함수를 호출하여 출구가 있는지 확인
    print(f'#{test_case} {result}')