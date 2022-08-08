# Programmers - Level2 - 더 맵게


import heapq            # 힙큐 모듈 사용을 위한 import


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)     # scoville 리스트를 힙으로 변환

    while len(scoville) > 1:    # 2개의 원소 비교를 위해 리스트 원소가 2개 이상일 경우에만 반복문 실행
        a = heapq.heappop(scoville)     # 최솟값 pop하여 a에 저장
        if a >= K:              # a가 K보다 같거나 크다면
            return answer       # answer를 리턴
        else:                   # 아닐 경우
            b = heapq.heappop(scoville)     # 최솟값 pop하여 b에 저장
            heapq.heappush(scoville, a + (b*2))     # a + (b*2)의 값을 push
            answer += 1         # answer 횟수 1회 증가

    if min(scoville) < K:       # 만약 반복문을 빠져나왔는데 최솟값이 K보다 작다면
        answer = -1             # answer에 -1을 저장
    return answer               # answer를 리턴
