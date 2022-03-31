import sys
sys.stdin = open("input.txt", "r")

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    bus_stop = list(map(int, input().split())) + [0]    # 정류소별 배터리 용량이 담긴 정보를 입력받아 bus_stop 리스트에 저장

    result = 0                                          # 결과를 출력하기 위한 result 변수 생성
    start = bus_stop[0]                                 # 출발지점을 맨 마지막 정류장을 지정
    while start > 1:                                    # 버스가 출발지에 도착하기 전까지 반복문 실행
        idx = -1                                        # 최대 이동 거리를 저장하기 위한 idx 변수 생성
        for i in range(start - 1, 0, -1):               # 현재 위치 전 정류장 부터 출발 정류장까지
            if bus_stop[i] + i >= start:                # 해당 정류장 배터리용량과 정류장 위치를 더한 값이 현재버스가 있는 정류장까지 올수 있으면
                idx = i                                 # idx에 i값을 대입
        if idx == -1:                                   # 만약 idx가 -1이라면
            result = 0                                  # result를 0으로 만들고
            break                                       # 반복문 종료
        start = idx                                     # start에 idx값으로 갱신
        result += 1                                     # result에 충전횟수 1을 더함

    print(f'#{test_case} {result - 1}')                 # 출발할때 충전은 횟수에서 제거하기 위해 result에 -1 한값을 출력