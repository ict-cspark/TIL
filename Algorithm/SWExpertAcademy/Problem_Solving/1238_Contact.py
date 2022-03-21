# 1238. [S/W 문제해결 기본] 10일차 - Contact

'''
비상연락망과 연락을 시작하는 당번에 대한 정보가 주어질 때,
가장 나중에 연락을 받게 되는 사람 중 번호가 가장 큰 사람을 구하는 함수를 작성하시오.
'''

import sys
sys.stdin = open("input.txt", "r")

def BFS(S):                                         # BFS를 수행하는 함수
    visit = [0] * 101                               # 방문 기록을 남기기위한 visit 리스트 생성
    queue = [S]                                     # 큐를 생성하고 초깃값으로 S를 저장

    visit[S] = 1                                    # 초깃값으로 visit[S] 에 1을 저장하고 시작
    answer = S                                      # 최댓값을 찾기 위해 answr 변수 생성하고 초기값 S로 설정
    while queue:                                    # 큐가 비어있지 않을 경우 while 반복문 계속 실행
        r = queue.pop(0)                            # 큐 리스트에서 맨 앞의 값을 꺼내와 r에 저장
        # 만약 visit[answer] 값보다 visit[r]의 값이 크거나
        # 혹은 두 값이 같지만 r의 값이 answer보다 크면
        if visit[answer] < visit[r] or (visit[answer] == visit[r] and answer < r):
            answer = r                              # answer에 r에 값을 대입

        for c in range(1, 101):                     # 해당 행의 열 갯수만큼 반복문 실행
            if arr[r][c] == 1 and visit[c] == 0:    # arr 해당 인덱스의 값이 1이고 방문한적이 없다면
                queue.append(c)                     # 큐에 c의 값을 추가하고
                visit[c] = visit[r] + 1             # visit[r]의 값에 1을 더한 값을 visit[c]에 저장

    return answer                                   # answer 결과 값을 return

# 테스트케이스 입력받기
T = 10

for test_case in range(1, T + 1):
    N, S = map(int, input().split())
    num = list(map(int, input().split()))

    arr = [[0] * 101 for _ in range(101)]           # 인접 2차원 행렬 리스트 생성

    for n in range(0, N, 2):                        # num에 저장된 인접 연결 정보를 2개씩 불러오기 위해 step을 2로 설정
        arr[num[n]][num[n + 1]] = 1                 # arr 행렬의 해당하는 위치에 1을 대입

    result = BFS(S)                                 # BFS 함수에 S값으로 호출한뒤 반환값을 result에 저장

    print(f'#{test_case} {result}')                 # 결과값 출력