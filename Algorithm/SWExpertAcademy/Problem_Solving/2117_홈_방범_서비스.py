# 2117. [모의 SW 역량테스트] 홈 방범 서비스

'''
홈방범 서비스를 제공받는 집들은 각각 M의 비용을 지불할 수 있어, 보안회사에서는 손해를 보지 않는 한 최대한 많은 집에 홈방범 서비스를 제공하려고 한다.
도시의 크기 N과 하나의 집이 지불할 수 있는 비용 M, 도시의 정보가 주어진다.
이때, 손해를 보지 않으면서 홈방범 서비스를 가장 많은 집들에 제공하는 서비스 영역을 찾고,
그 때의 홈방범 서비스를 제공 받는 집들의 수를 출력하는 프로그램을 작성하라.
'''

import sys
sys.stdin = open("input.txt", "r")


def check(arr):                                                 # check 함수 실행 (정석적인 방법)
    result = 0                                                  # 결과값 저장을 위한 변수 생성
    for sr in range(N):                                         # N의 길이만큼 가로, 세로 반복문 실행
        for sc in range(N):
            for k in range(1, (2 * N) + 1):                     # 1 부터 2*N 까지 k 반복문 실행
                answer = 0                                      # 집 갯수 임시 저장을 위한 answer 변수 생성
                for r in range((sr - k) + 1, sr + k):           # k 서비스 영역 가로 길이만큼 반복문 실행
                    # k 서비스 영역 세로 길이만큼 반복문 실행 ( 십자가 형태를 위해 r - sr의 절댓값을 이용 )
                    for c in range((sc - k) + 1 + abs(r - sr), sc + k - abs(r - sr)):
                        # 만약 r, c가 인덱스 범위내이고 해당 좌표에 집이 있을 경우
                        if 0 <= r < N and 0 <= c < N and arr[r][c] == 1:
                            answer += 1                         # answer에 1을 추가
                # 반복문 종료 후 수익이 운영비용보다 같거나 크고 answer의 값이 result 보다 클 경우
                if cost[k] <= answer * M and result < answer:
                    result = answer                             # result 값 갱신

    return result                                               # result를 리턴


def fast_check(arr):                                            # 개선 된 두 번째 방법을 위한 fast_check 함수
    home = []                                                   # 집이 있는 위치를 저장하기 위한 home 리스트 생성
    for i in range(N):                                          # arr 배열을 탐색하면서 집의 인덱스 정보를 home리스트에 저장
        for j in range(N):
            if arr[i][j] == 1:
                home.append([i, j])
    result = 0                                                  # 결과를 저장하기 위한 result 변수 생성
    for sr in range(N):                                         # arr 배열을 탐색하기 위한 반복문 실행
        for sc in range(N):
            cnt = [0] * ((2 * N) + 1)                           # 현재 위치에서 집의 거리를 저장하기 위한 cnt 리스트 생성
            for r, c in home:                                   # home에 저장된 인덱스 정보를 불러와 반복문 실행
                idx = abs(sr - r) + abs(sc - c) + 1             # 집과 현재 위치의 인덱스 차이를 계산 (출발지부터 1을 세기 때문에 1추가)
                cnt[idx] += 1                                   # cnt[idx] 값의 1을 추가
            compare = cnt[:]                                    # 누적합을 위해 compare리스트 생성
            for i in range(1, len(cnt)):                        # cnt 길이만큼 반복문을 1부터 끝까지 실행
                compare[i] = compare[i] + compare[i - 1]        # 현재 값의 이전값을 더해 저장

            for j in range(1, len(compare)):                    # compare 리스트 길이만큼 반복문 실행
                # 만약 운영비용보다 수익이 크고 comapre[j]의 값이 result 보다 크다면
                if cost[j] <= compare[j] * M and result < compare[j]:
                    result = compare[j]                         # result 값에 compare[j] 값을 저장

    return result                                               # result를 리턴


# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())                            # 도시 크기와 비용 N, M 입력받기
    city = [list(map(int, input().split())) for _ in range(N)]  # 집의 좌표가 담긴 city 이차원 배열 생성
    cost = [0] + [((K * K) + ((K - 1) * (K - 1))) for K in range(1, (2 * N) + 1)]   # 서비스 영역 K 마다 운영 비용이 담긴 리스트 생성

    # result = check(city)                                      # check 함수 실행하여 result에 저장
    result = fast_check(city)                                   # fast_check 함수 실행하여 result에 저장

    print(f'#{test_case} {result}')                             # 결과 값 출력