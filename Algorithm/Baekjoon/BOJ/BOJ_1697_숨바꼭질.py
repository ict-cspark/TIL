# Baekjoon Online Judge - 숨바꼭질

'''
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고,
동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다.
만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
'''


def BFS(N, K):                                  # BFS 함수 실행
    checked = [0] * 100001                      # chekced 리스트 생성
    queue = [N]                                 # 큐리스트 생성 후 N에 저장
    while queue:                                # 큐리스트가 비어있을 때까지 반복문 실행
        start = queue.pop(0)                    # 큐에 첫번째 요소를 꺼내 start에 저장
        if start == K:                          # 만약 start가 K와 같다면
            return checked[start]               # checkd[start] 값 리턴
        # 만약 start + 1의 값이 0과 10만 사이이고 값이 나온적이 없다면
        if 0 <= start + 1 <= 100000 and checked[start + 1] == 0:
            queue.append(start + 1)             # 큐에 값 추가하고
            checked[start + 1] = checked[start] + 1 # checked[start + 1] 위치에 checked[start] 값에서 + 1한 값을 저장
        if 0 <= start - 1 <= 100000 and checked[start - 1] == 0:
            queue.append(start - 1)
            checked[start - 1] = checked[start] + 1
        if 0 <= start * 2 <= 100000 and checked[start * 2] == 0:
            queue.append(start * 2)
            checked[start * 2] = checked[start] + 1


N, K = map(int, input().split())                # 시작값과 목표값 N, K 입력받기
    
result = BFS(N, K)                              # BFS 함수 실행하고 리턴값 result에 저장
print(result)                                   # 결과값 출력
