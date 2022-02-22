# 1945. 간단한 소인수분해

'''
숫자 N은 아래와 같다.

N=2a x 3b x 5c x 7d x 11e

N이 주어질 때 a, b, c, d, e 를 출력하라.
'''

import sys
sys.stdin = open("input.txt", "r")

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):

    # 숫자 입력 받고 소인수분해를 위한 prime 리스트 생성하고 결과값 저장을 위한 result 리스트 생성
    num = int(input())
    prime = [2, 3, 5, 7, 11]
    result = [0, 0, 0, 0, 0]

    # prime 리스트 길이만큼 반복하여
    # num이 소수로 나눠질경우 
    # num을 해당 소수로 나누고 해당 인덱스에 위치한 결과값 리스트에 1추가
    for p in range(5):
        while num%prime[p] == 0:
            num = num/prime[p]
            result[p] += 1

    # 결과값 출력
    result = " ".join(map(str, result))
    print(f'#{test_case} {result}')
