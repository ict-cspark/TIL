import sys
sys.stdin = open("input.txt", "r")

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N, E = map(int, input().split())                    # 정점의 갯수 N과 간선의 갯수 E 입력 받기
    queue = sorted([list(map(int, input().split())) for _ in range(E)])   # 도로 정보 입력받아 queue에 정렬하여 저장
    print(queue)

    distance = [0] + [1000000] * E                      # 0번은 0으로 초기화하고 나머지는 1000000으로 초기화하여 거리 리스트 생성
    while queue:                                        # 큐가 비어있지 않을때까지 반복문 실행
        s, e, w = queue.pop(0)                          # 앞에서부터 큐를 하여 s, e, w에 각각 저장
        if distance[e] > distance[s] + w:               # 이전 거리에서 현재 구간거리의 합이 현재 저장된 값보다 작다면
            distance[e] = distance[s] + w               # 값 갱신

    print(f'#{test_case} {distance[N]}')                # 마지막 정점의 구간거리 합을 출력