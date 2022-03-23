# Baekjoon Online Judge - 프린터 큐

'''
여러분이 할 일은, 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때,
어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다.
예를 들어 위의 예에서 C문서는 1번째로, A문서는 3번째로 인쇄되게 된다.
'''

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N, I = map(int, input().split())                # 문서의 갯수 N과 확인할 프린터 번호 I 입력 받기
    im = list(map(int, input().split()))            # 문서의 중요도 입력받기

    queue = []                                      # 중요도에 따라 프린트를 실행할 큐 리스트 생성
    for i in range(N):                              # 문서갯수만큼 반복문 실행
        queue.append((im[i], i))                    # 문서 중요도와 문서번호를 함께 큐에 순서대로 저장

    c = 0                                           # 프린트 횟수를 저장하기 위한 변수 선언
    while queue:                                    # 큐가 비어있지 않을때까지 반복문 실행
        p = queue.pop(0)                            # 큐에 첫번째 요소를 pop하여 p에 저장
        if queue and p[0] < max(queue)[0]:          # 만약 큐가 비어있지 않고 p의 중요도가 큐에 있는 문서의 중요도보다 작다면
            queue.append(p)                         # 큐에 다시 추가
        else:
            c += 1                                  # 만약 p의 중요도가 가장 크다면 문서횟수 1 추가
            if p[1] == I:                           # 만약 p의 문서번호가 I와 일치하다면
                print(c)                            # c를 출력
                break                               # 반복문 종료