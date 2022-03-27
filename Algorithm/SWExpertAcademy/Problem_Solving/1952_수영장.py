# 1952. [모의 SW 역량테스트] 수영장

'''
각 이용권의 요금과 각 달의 이용 계획이 입력으로 주어질 때,
가장 적은 비용으로 수영장을 이용할 수 있는 방법을 찾고 그 비용을 정답으로 출력하는 프로그램을 작성하라.
'''

import sys
sys.stdin = open("input.txt", "r")


def DFS(n, answer):                                 # DFS 함수 호출
    global result                                   # result global 변수로 호출
    if n > 12:                                      # n이 12보다 클 경우 아래 조건문 실행
        if result > answer:                         # result값이 answer보다 클경우
            result = answer                         # result 값 answer로 교체 후 return
        return

    DFS(n + 1, answer + (plan[n] * d))              # n에 1을 더하고 answer에 해당월 계획일수와 일일요금 곱한 값 추가 
    DFS(n + 1, answer + m)                          # n에 1을 더하고 answer에 한달 요금 추가 
    DFS(n + 3, answer + t)                          # n에 3을 더하고 answer에 3개월 요금 추가 
    DFS(n + 12, answer + y)                         # n에 12을 더하고 answer에 1년 요금 추가 


# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    d, m, t, y = map(int, input().split())          # 1일, 한달, 3개월, 1년 요금 입력 받기
    plan = [0] + list(map(int, input().split()))    # 수영장 이용 계획 달별로 입력받아 리스트에 저장
    result = 987654321                              # 임의의 큰수 result 입력 받기
    DFS(1, 0)                                       # DFS 함수 호출하고 1월 부터 요금 0원으로 설정

    print(f'#{test_case} {result}')                 # 결과값 호출