import sys
sys.stdin = open("input.txt", "r")


def search(r, c, value, N):                         # search 함수 실행
    global result                                   # result 리스트 global로 호출
    if r == N - 1 and c == N - 1:                   # 만약 r과 c의 값이 도착 위치일 경우
        value += arr[r][c]                          # 도착지의 숫자를 value에 더하고
        result.append(value)                        # value를 result에 추가

    else:
        if 0 <= r < N and 0 <= c < N:               # 만약 r과 c가 인덱스 범위 내일 경우
            search(r + 1, c, value + arr[r][c], N)  # 아래로 이동한 경로 정보와 value에 현재 위치 숫자를 더해서 호출
            search(r, c + 1, value + arr[r][c], N)  # 오른쪽으로 이동한 경로 정보와 value에 현재 위치 숫자를 더해서 호출

    return


# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())                                # 판의 길이 N 입력 받기
    arr = [list(map(int, input().split())) for _ in range(N)]   # 판의 정보 arr 리스트에 입력 받기

    result = []                                     # 경로 합을 저장할 result 리스트 생성
    search(0, 0, 0, N)                              # search 함수 실행 (출발 위치 0, 0 과 경로 합 0, 판의 길이 N)

    print(f'#{test_case} {min(result)}')            # result에 저장된 리스트 중에 최솟값 출력