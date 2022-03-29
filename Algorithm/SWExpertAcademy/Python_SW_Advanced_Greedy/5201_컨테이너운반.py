import sys
sys.stdin = open("input.txt", "r")

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):   
    N, M = map(int, input().split())                    # 컨테이너 갯수 N과 트럭 갯수 M 입력 받기
    weight = list(map(int, map(int, input().split())))  # 컨테이너 무게 입력받아 weight 리스트에 저장
    truck = list(map(int, map(int, input().split())))   # truck 적재 용량 입력받아 truck 리스트에 저장

    weight.sort(reverse=True)                           # 컨테이너 무게 내림차순으로 정렬
    truck.sort(reverse=True)                            # 트럭 적재용량 내림차순으로 정렬

    result = 0                                          # 결과 저장을 위한 result 변수 생성
    for n in range(N):                                  # 컨테이너 갯수만큼 반복문 실행
        for m in truck[:]:                              # truck 리스트의 갯수가 변할 수 있기 때문에 얕은 복사로 반복문 실행
            if weight[n] <= m:                          # 만약 컨테이너 무게보다 트럭 적재용량이 크다면
                result += weight[n]                     # 현재 컨테이너 무게를 result에 추가
                truck.remove(m)                         # 트럭리스트에서 현재 트럭을 제거
                break                                   # 반복문 종료 후 다음 컨테이너 실행

    print(f'#{test_case} {result}')                     # 결과값 출력