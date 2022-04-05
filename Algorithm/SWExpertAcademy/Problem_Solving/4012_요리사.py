# 4012. [모의 SW 역량테스트] 요리사

'''
식재료 i를 식재료 j와 같이 요리하게 되면 발생하는 시너지 Sij의 정보가 주어지고,
가지고 있는 식재료를 이용해 A음식과 B음식을 만들 때,
두 음식 간의 맛의 차이가 최소가 되는 경우를 찾고 그 최솟값을 정답으로 출력하는 프로그램을 작성하라.
'''

import sys
sys.stdin = open("input.txt", "r")


def DFS(K, a, b):                                       # DFS 함수 호출 (시작값 K와 A,B음식 재료 담을 리스트)
    global result                                       # result 변수 global로 호출

    if K == N:                                          # K와 N이 같을 경우 아래 조건문 실행
        if len(a) == len(b):                            # 만약 a와 b 리스트의 길이가 같을 경우
            asum = 0                                    # 시너지값 저장을 위한 asum, bsum 생성
            bsum = 0
            for i in range(len(a)):                     # a리스트 길이만큼 2중 반복문 실행하여
                for j in range(len(a)):
                    asum += food[a[i]][a[j]]            # food[a[i]][a[j]] 값을 asum에 저장
                    bsum += food[b[i]][b[j]]            # food[b[i]][b[j]] 값을 bsum에 저장
            answer = abs(asum - bsum)                   # 두 시너지 합의 차이를 answer에 저장
            if result > answer:                         # 만약 result 보다 answer가 작다면
                result = answer                         # 값 갱신 후 리턴
        return
    else:
        DFS(K + 1, a + [K], b)                          # K+1과 a리스트에 K값을 더해 DFS 재호출
        DFS(K + 1, a, b + [K])                          # K+1과 b리스트에 K값을 더해 DFS 재호출


# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())                                    # 식재료의 갯수 N 입력받기
    food = [list(map(int, input().split())) for _ in range(N)]  # 식재료 시너지 정보 입력받아 food 리스트에 저장

    result = 987654321                                  # 두 음식의 시너지 차이를 저장하기 위한 result 변수 생성
    DFS(0, [], [])                                      # DFS 함수 호출

    print(f'#{test_case} {result}')                     # 결과값 출력