import sys                          # sys.stdin.readline 을 사용하기 위해
N = int(sys.stdin.readline())

tree = [[] for _ in range(N + 1)]   # tree 리스트 생성

for _ in range(N - 1):              # N - 1번만큼 반복문 실행
    x, y = map(int, sys.stdin.readline().split())
    tree[x].append(y)               # tree[x]에 y값 추가
    tree[y].append(x)               # tree[y]에 x값 추가

parent = [0] * (N + 1)              # 부모 리스트 생성

parent[1] = -1                      # 루트노드에 -1로 초기화
queue = [1]                         # 큐에 초기값 대입
while queue:                        # 큐가 비어있지 않을 때가지 반복문 실행
    r = queue.pop(0)                # r에 큐에 첫번째 요소 pop
    for c in tree[r]:               # tree[r]에서 요소 갯수만큼 반복문 실행
        if parent[c] == 0:          # parent[c] 가 0이라면
            queue.append(c)         # queue에 c를 append
            parent[c] = r           # parent[c] 에 r값 대입

for i in range(2, N + 1):           # 2부터 마지막까지 반복문 실행
    print(parent[i])                # parent[i] 출력