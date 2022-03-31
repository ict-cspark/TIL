import sys
sys.stdin = open("input.txt", "r")


def Binary(num):                                    # Binary 함수
    global result                                   # result 변수 global로 호출
    start = 0                                       # start 변수 생성하고 0으로 초기화
    end = N - 1                                     # end 변수 생성하고 N - 1로 초기화

    flag = 0                                        # 이전 상태 확인을 위한 flag 변수 생성
    while start <= end:                             # start가 end보다 크지 않을 경우 반복문 계속 실행
        mid = (start + end) // 2                    # mid에 (start + end) // 2 값 대입
        if A[mid] == num:                           # 만약 A[mid]와 num이 같다면 result에 1을 더하고 함수 종료
            result += 1
            return
        elif A[mid] > num:                          # 만약 num이 더 작다면 왼쪽으로 탐색하기 위해서
            end = mid - 1                           # end를 mid - 1 인덱스로 변경
            if flag == 1:                           # 혹시 flag가 1이라면 함수 종료
                return
            flag = 1                                # 왼쪽으로 이동할경우 flag를 1로 변경
        else:                                       # 만약 num이 더 크다면 오른쪽으로 탐색하기 위해서
            start = mid + 1                         # start를 mid + 1 인덱스로 변경
            if flag == 2:                           # 혹시 flag가 2라면 함수 종료
                return
            flag = 2                                # 오른쪽으로 이동하면 flag 2로 변경


# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())                # A와 B의 원소 갯수 N, M 입력받기
    A = sorted(list(map(int, input().split())))     # A의 숫자 입력받아 정렬 후 A 리스트 저장
    B = list(map(int, input().split()))             # B의 숫자 입력받아 B 리스트 저장

    result = 0                                      # 결과 갯수를 세기 위한 result 생성
    for i in B:                                     # B 리스트의 값들을 하나씩 불러오기
       Binary(i)                                    # Binary 함수 호출

    print(f'#{test_case} {result}')                 # result 출력