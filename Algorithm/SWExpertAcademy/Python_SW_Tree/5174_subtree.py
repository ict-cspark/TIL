import sys
sys.stdin = open("input.txt", "r")

def root(N):                # N을 루트로 하는 노드의 갯수를 알아내는 함수
    global result           # 결과값 저장을 위한 result 변수를 global로 설정
    if N:                   # N이 0이 아닐 경우 아래 조건문 실행
        result += 1         # result에 1을 더함
        root(left[N])       # left[N]의 값으로 함수 호출
        root(right[N])      # right[N]의 값으로 함수 호출


# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    V = E + 1               # 정점의 갯수를 구하기 위해 간선에 1을 더한 값을 저장

    left = [0] * (V + 1)    # 왼쪽 자식 노드를 알아내기 위한 0으로 채운 리스트 생성
    right = [0] * (V + 1)   # 오른쪽 자식 노드를 알아내기 위한 0으로 채운 리스트 생성

    for e in range(E):      # 간선의 갯수 만큼 반복문 실행
        # 첫번째 값을 부모 노드로, 두번째 값을 자식 노드로 각각 대입
        P, C = arr[(2 * e)], arr[(2 * e) + 1]
        if left[P] == 0:    # 왼쪽 자식 노드가 비어있을 경우 자식 노드 값 대입
            left[P] = C
        else:
            right[P] = C    # 오른쪽 자식 노드가 비어있을 경우 자식 노드 값 대입

    result = 0              # 결과값 저장을 위한 빈 변수 생성
    root(N)                 # 루트 N으로 하는 함수 호출

    print(f'#{test_case} {result}') # 결과값 출력