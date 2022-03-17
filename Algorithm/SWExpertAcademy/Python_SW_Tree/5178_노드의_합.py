import sys
sys.stdin = open("input.txt", "r")

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())

    num = [0] * (N + 1)                 # 노드의 합을 저장하기 위한 빈 리스트 생성
    for _ in range(M):                  # 리프 노드에 저장 된 값을 num 리스트에 저장
        leaf, number = map(int, input().split())
        num[leaf] = number

    for n in range(N, 0, -1):           # 노드 마지막 번호부터 1까지 역으로 반복문 실행
        left = 0                        # 왼쪽, 오른쪽 값을 저장하기 위한 빈 변수 선언
        right = 0
        if num[n] == 0:                 # num[n]의 값이 0일 때만 아래 조건문 실행
            if 0 < 2 * n < N + 1:       # 왼쪽 자식 노드의 값이 인덱스 범위 내에 있을 경우
                left = num[2 * n]       # left에 값 저장
            if 0 < (2 * n) + 1 < N + 1: # 오른쪽 자식 노드의 값이 인덱스 범위 내에 있을 경우
                right = num[(2 * n) + 1]    # right에 값 저장

            num[n] = left + right       # 부모 노드에 left와 right의 값을 저장

    result = num[L]                     # result에 지정한 노드 번호의 저장된 값을 저장
    print(f'#{test_case} {result}')     # 결과 출력