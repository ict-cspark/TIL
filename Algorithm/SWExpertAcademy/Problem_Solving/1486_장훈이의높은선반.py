# 1486. 장훈이의 높은 선반

'''
장훈이는 서점을 운영하고 있다.
서점에는 높이가 B인 선반이 하나 있는데 장훈이는 키가 매우 크기 때문에, 선반 위의 물건을 자유롭게 사용할 수 있다.
어느 날 장훈이는 자리를 비웠고, 이 서점에 있는 N명의 점원들이 장훈이가 선반 위에 올려놓은 물건을 사용해야 하는 일이 생겼다.
각 점원의 키는 Hi로 나타나는데, 점원들은 탑을 쌓아서 선반 위의 물건을 사용하기로 하였다.
점원들이 쌓는 탑은 점원 1명 이상으로 이루어져 있다.
탑의 높이는 점원이 1명일 경우 그 점원의 키와 같고, 2명 이상일 경우 탑을 만든 모든 점원의 키의 합과 같다.
탑의 높이가 B 이상인 경우 선반 위의 물건을 사용할 수 있는데 탑의 높이가 높을수록 더 위험하므로 높이가 B 이상인 탑 중에서 높이가 가장 낮은 탑을 알아내려고 한다.
'''

import sys
sys.stdin = open("input.txt", "r")


def DFS(K, S):                                  # DFS 함수, 시작값 K와 키의 합 S
    global result                               # result global로 호출
    if S - B >= result:                         # 만약 목표값과의 차가 result 보다 크다면 함수 종료
        return
    if K == N:                                  # K와 N이 같을 때
        if S >= B:                              # 목표값보다 키의 합이 크거나 같을 경우
            answer = S - B                      # 두 값의 차를 answer에 저장
            if result > answer:                 # 만약 result보다 answer가 더 작다면
                result = answer                 # result 값 갱신
        return                                  # 함수 종료
    else:
        P[K] = 0
        DFS(K + 1, S)
        P[K] = 1
        DFS(K + 1, S + H[K])

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N, B = map(int, input().split())            # 직원 수와 목표 높이 입력받기 
    H = list(map(int, input().split()))         # 직원 키 입력 받기
    P = [0] * N                                 # 부분 집합을 만들기 위한 P 리스트 생성

    result = 987654321                          # 결과값을 찾기 위한 result 변수 생성
    DFS(0, 0)                                   # DFS함수 호출

    print(f'#{test_case} {result}')             # 결과값 출력