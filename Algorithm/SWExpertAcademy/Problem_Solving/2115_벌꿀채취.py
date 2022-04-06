# 2115. [모의 SW 역량테스트] 벌꿀채취

'''
벌통들의 크기 N과 벌통에 있는 꿀의 양에 대한 정보, 선택할 수 있는 벌통의 개수 M, 꿀을 채취할 수 있는 최대 양 C가 주어진다.
이때 두 일꾼이 꿀을 채취하여 얻을 수 있는 수익의 합이 최대가 되는 경우를 찾고, 그 때의 최대 수익을 출력하는 프로그램을 작성하라.
'''

import sys
sys.stdin = open("input.txt", "r")


def DFS(K, cnt, S, arr):                                            # DFS 함수 실행 (시작값 K, 꿀의 양, 수익, 채취한 벌통 리스트)
    global answer                                                   # answer를 global로 호출

    if K == M:                                                      # K와 M이 같을 경우 아래 조건문 실행
        if cnt <= C and answer < S:                                 # 꿀의 양이 최대양보다 같거나 작고 수익이 answer보다 크다면
            answer = S                                              # answer값 S로 갱신후 리턴
            return
    else:
        DFS(K + 1, cnt, S, arr)                                     # 경우의 수를 구하기 위해 K + 1을 하고 기존값 그대로 호출
        DFS(K + 1, cnt + arr[K], S + (arr[K] ** 2), arr)            # K + 1을 하고 꿀의 양에 arr[K]값을 더하고 수익에 arr[K]의 값의 제곱을 더해 호출

    return


# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N, M, C = map(int, input().split())                             # 벌통의 크기와 갯수 꿀의 양 N, M, C 입력 받기
    honey = [list(map(int, input().split())) for _ in range(N)]     # 꿀의 양이 담긴 정보를 입력받아 honey에 저장

    result = 0                                                      # 결과를 저장하기 위한 result 변수 생성
    for i in range(N):                                              # 일꾼1의 채취 범위를 구하기 위한 반복문 실행
        for j in range(0, (N - M) + 1):                             # 가로의 크기는 N - M + 1 까지로 설정
            answer = 0                                              # 채취한 꿀의 최댓값을 저장하기 위한 answer 변수
            DFS(0, 0, 0, honey[i][j:j + M])                         # 일꾼1이 채취한 꿀의 최댓값을 구하기 위한 DFS 함수 실행
            ans1 = answer                                           # answer에 값을 ans1에 저장

            for ii in range(i, N):                                  # 일꾼2의 채취 범위를 구하기 위한 반복문 실행
                sj = 0                                              # 일꾼1과 같은 행에 있는지 판단하기 위한 sj 변수 생성
                if i == ii:                                         # 만약 일꾼 1과 같은 행에 있을 경우 sj의 값을 j + M으로 변경
                    sj = j + M
                for jj in range(sj, (N - M) + 1):                   # 일꾼2의 가로 크기는 sj 부터 N - M + 1로 설정
                    answer = 0                                      # 채취한 꿀의 최댓값을 저장하기 위한 answer 변수
                    DFS(0, 0, 0, honey[ii][jj:jj + M])              # 일꾼2가 채취한 꿀의 최댓값을 구하기 위한 DFS 함수 실행
                    ans2 = answer                                   # answer에 값을 ans2에 저장
                    if result < ans1 + ans2:                        # ans1 + ans2의 값이 result보다 크다면
                        result = ans1 + ans2                        # result 값 갱신

    print(f'#{test_case} {result}')                                 # 결과값 출력