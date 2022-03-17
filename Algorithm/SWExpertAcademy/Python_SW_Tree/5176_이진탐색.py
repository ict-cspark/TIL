import sys
sys.stdin = open("input.txt", "r")

def in_order(V):                # 중위 순회를 구현하는 함수
    global visit                # 방문 순서를 남기기 위한 global 변수 선언
    if 0 <= V < N + 1:          # V가 노드 범위 내에 있을경우 아래 조건문 실행
        in_order(V * 2)         # 왼쪽 자식 노드를 방문하는 함수 호출
        visit += 1              # 방문 순서에 1을 더하고
        tree[V] = visit         # 현재 노드에 visit 값을 저장
        in_order((V * 2) + 1)   # 오른쪽 자식 노드를 방문하는 함수 호출


# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)        # 방문 순서를 기록하기 위한 트리 리스트 생성

    visit = 0                   # 방문 순서를 남기기 위한 초기 변수 선언
    in_order(1)                 # 중위 순회 함수 호츨

    print(f'#{test_case} {tree[1]} {tree[N//2]}') # 결과값 출력