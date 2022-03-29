import sys
sys.stdin = open("input.txt", "r")

# 테스트케이스 입력받기
T = int(input())


def method(s, K):                               # 순열을 구하기 위한 method 함수 (초기 위치 s, 갯수 K)
    global answer                               # answer를 global로 호출
    if s == K:                                  # s와 K가 같을 경우
        answer.append([0] + p + [0])            # 저장된 p에 앞 뒤로 0을 더해 answer에 추가
    else:
        for i in range(K):                      # K번까지 반복문 실행
            if visited[i] == 0:                 # 방문한적이 없다면
                visited[i] = 1                  # 방문 흔적을 남기고
                p[s] = num[i]                   # p[s]에 num[i] 값을 저장하고
                method(s + 1, K)                # s + 1을 하여 재호출
                visited[i] = 0                  # 함수 종료되면 방문 흔적을 지우기

    return


def search(arr):                                # 배터리 소비량 구하기 위한 serch 함수
    global result                               # 소비량 저장을 위해 result를 global로 호출
    for a in arr:                               # arr에 담긴 갯수만큼 반복문 실행
        value = 0                               # 소비량 합을 구하기 위한 value 변수 생성
        for i in range(N):                      # N 만큼 반복문 실행
            value += field[a[i]][a[i + 1]]      # value에 field[a[i]][a[i + 1]] 더함

        result.append(value)                    # result에 value 값 저장
    return


for test_case in range(1, T + 1):
    N = int(input())                            # 관리구역 번호 입력받기
    field = [list(map(int, input().split())) for _ in range(N)] # 배터리 사용량 표 입력받아 field에 저장
    num = [i for i in range(1, N)]              # 이동 경로를 조합하기 위한 num 리스트 생성
    p = [0] * (N - 1)                           # 순열을 담기 위한 p 리스트 생성
    visited = [0] * (N - 1)                     # 순열을 만들면서 사용한적이 있는지 확인할 visited 리스트 생성

    answer = []                                 # 모든 이동경로를 저장하기 위한 answer 리스트 생성
    method(0, N - 1)                            # method 함수 호출, 사무실 제외하기 위해 N - 1 대입

    result = []                                 # 배터리 사용량을 담을 result 리스트 샏성
    search(answer)                              # serach 함수 호출

    print(f'#{test_case} {min(result)}')        # result 리스트의 최솟값을 출력