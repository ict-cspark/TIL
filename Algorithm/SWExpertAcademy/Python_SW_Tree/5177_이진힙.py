import sys
sys.stdin = open("input.txt", "r")

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())                        # 변수 N을 생성하여 노드 갯수 저장
    num = list(map(int, input().split()))   # 서로 다른 자연수를 저장하기 위한 num 리스트 생성
    tree = [0] * (N + 1)                    # 이진 힙을 저장하기 위한 tree 리스트 생성
    tree[1] = num[0]                        # 루트 노드의 초기값으로 num의 첫번째 값 저장

    for n in range(1, N):                   # num의 저장된 2번째 값부터 마지막 값까지 반복문 실행
        t = n + 1                           # 트리 리스트는 인덱스와 맞추었기 때문에 1을 더함
        tree[t] = num[n]                    # 트리[t]에 num[n] 값을 저장
        while t > 1:                        # 루트 노드까지 값을 비교해야 하기 때문에 while문 실행
            if tree[(t//2)] > tree[t]:      # 만약 조상노드가 자식노드보다 크다면
                tree[(t//2)], tree[t] = tree[t], tree[(t//2)]   # 값을 서로 바꿈
            t = t // 2                      # 조상노드로 가기 위해 2로 나는 몫을 t에 저장

    result = 0                              # 결과값 저장을 위한 result 변수 생성
    while N > 1:                            # 루트 노드까지 while 반복문 실행
        N = N // 2                          # 조상을 찾기 위해 N에 2로 나눈 몫을 저장
        result += tree[N]                   # tree[N]의 값을 result에 저장

    print(f'#{test_case} {result}')         # 결과값 출력