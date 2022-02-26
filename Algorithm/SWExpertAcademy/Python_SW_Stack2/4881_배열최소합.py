import sys
sys.stdin = open("input.txt", "r")

def check_Min(r, arr_Sum):          # check_Min 함수 생성
    global arr_Min                  # arr_Min을 global을 이용하여 함수 내에서 사용
    if arr_Min <= arr_Sum:          # 만약 Min 값이 Sum 값보다 작다면 아래 조건문실행하지 않고 return
        return

    elif r == N:                    # 행의 값이 N과 같다면 (즉, 모든 행을 실행했다면) 아래 조건문 실행
        if arr_Min > arr_Sum:       # Sum의 값이 더 작다면 Min 값에 대입 후 return
            arr_Min = arr_Sum
        return
    else:
        for c in range(N):          # 열 길이만큼 반복
            if select[c] == 0:      # 선택되지않은 열이면 해당 인덱스에 1을 대입하고
                select[c] = 1       # 다음 행과, Sum 값에 현재 위치의 원소값을 더한 값으로 함수 재호출
                check_Min(r + 1, arr_Sum + arr[r][c])
                select[c] = 0       # return 후 빠져나왔을 경우 해당 열을 0으로 바꾼 후
                                    # 만약 현재 열의 위치가 마지막이 아니라면 for 반복문을 다시실행하고
    return                          # 마지막이라면 반복문을 빠져나와 return

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())                    # 배열의 크기 N과 배열을 입력받아 이차원 행렬 arr로 만들기
    arr = [list(map(int, input().split())) for _ in range(N)]

    select = [0] * N                    # 중복 선택을 피하기위해 select 리스트 생성
    arr_Min = 9876543210                # 최솟값을 찾기 위해 초기값으로 큰수를 설정하고 변수 생성
    check_Min(0, 0)                     # check_Min 함수를 호출하고 행 시작값과 SUM 초기값 설정

    print(f'#{test_case} {arr_Min}')    # 결과값 출력