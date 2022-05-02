# 5688. 세제곱근을 찾아라

'''
양의 정수 N에 대해 N = X3가 되는 양의 정수X 를 구하여라.
'''

import sys
sys.stdin = open("input.txt", "r")


# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())                            # 목표값 N 입력 받기

    result = -1                                 # 결과값 출력을 위한 result 변수 생성하고 -1로 초기화
    K = 1                                       # 세제곱근을 찾기위한 K 생성후 1로 초기화
    while K ** 3 <= N:                          # K의 세제곱이 N보다 작거나 같을때까지 반복문 실행
        if K ** 3 >= N:                         # 만약 K의 세제곱이 N보다 같거나 클 경우 아래 조건문 실행
            if K ** 3 == N:                     # K의 세제곱이 N과 같다면
                result = K                      # result에 K로 갱신하고 
            break                               # 반복문 종료
        else:
            K += 1                              # K 세제곱이 N보다 작을 경우 K에 1을 더하고 다음 반복문 실행


    print(f'#{test_case} {result}')             # 결과값 출력