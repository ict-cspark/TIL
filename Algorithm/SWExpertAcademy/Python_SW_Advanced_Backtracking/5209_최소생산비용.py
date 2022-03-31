import sys
sys.stdin = open("input.txt", "r")


def DFS(k, S):                                          # DFS 함수 실행 (출발 인덱스, 생산비용 합)
    global result                                       # result를 global 변수로 호출

    if k == N:                                          # k와 N이 같을 경우
        if result > S:                                  # result보다 S가 작을 경우
            result = S                                  # result 값을 S로 갱신

    if S > result:                                      # 백트래킹
        return                                          # 생산비용이 현재 저장된 result 보다 클경우 함수 종료

    for i in range(N):                              # N 번 반복문 실행
        if check[i] == 0:                           # i번째를 사용한 적이 없다면
            check[i] = 1                            # 사용흔적을 남기고
            DFS(k + 1, S + product[k][i])           # DFS 함수를 호출하면서 k + 1, S에 product[k][i] 생산비용을 더해서 호출
            check[i] = 0                            # 다른 순열을 만들기 위해 사용흔적 다시 제거


# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())                                    # 제품의 갯수 N 입력받기
    product = [list(map(int, input().split())) for _ in range(N)] # 공장별 생산비용 입력받아 product에 저장

    result = 987654321                                  # 최소비용을 구하기 위한 result 변수 생성
    check = [0] * N                                     # 순열을 구하기 위한 check 리스트 생성
    DFS(0, 0)                                           # DFS 함수 실행

    print(f'#{test_case} {result}')                     # 결과값 출력