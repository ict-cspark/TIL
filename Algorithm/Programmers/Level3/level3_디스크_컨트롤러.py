# Programmers - Level3 - 디스크 컨트롤러

import heapq


def solution(jobs):
    answer = 0              # answer 변수 생성
    start = -1              # start 변수 생성 후 -1로 초기화
    end = 0                 # end 변수 생성 후 0으로 초기화
    idx = 0                 # idx 변수 생성 후 0으로 초기화
    heap = []               # 힙 생성

    while idx < len(jobs):  # idx가 리스트 길이 보다 작을 경우 반복문 실행
        for j in jobs:      # jobs 리스트로 반복문 실행하여
            if start < j[0] <= end:     # 만약 j[0]의 요청시간이 start와 end 이내라면
                heapq.heappush(heap, (j[1], j[0]))  # heap에 (j[1], j[0]) 튜플 추가

        if heap:            # heap이 있을 경우
            work, request = heapq.heappop(heap)  # heap에서 꺼내와 work와 request에 저장
            start = end     # start를 end로 변경
            end += work     # end에 작업시간 더하기
            answer += end - request     # answer에 end를 더하고 요청시간만큼 빼기
            idx += 1        # idx 1 추가
        else:               # 힙이 비어있을 경우 end에 1을 더하기
            end += 1

    return answer // idx    # answer에서 idx 나눈 몫을 리턴
