# 4837. [파이썬 S/W 문제해결 기본] 2일차 - 부분집합의 합
'''
1부터 12까지의 숫자를 원소로 가진 집합 A가 있다. 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.
해당하는 부분집합이 없는 경우 0을 출력한다. 모든 부분 집합을 만들어 답을 찾아도 된다.
예를 들어 N = 3, K = 6 경우, 부분집합은 { 1, 2, 3 } 경우 1가지가 존재한다.
'''

import sys
sys.stdin = open('input.txt', 'r')

# 테스트 케이스 입력 받습니다.
T = int(input())

for t in range(1, T+1):
    # N, K를 입력 받습니다.
    N, K = map(int, input().split())

    result = 0
    # 비트 연산을 이용해 부분집합의 총 갯수를 구합니다.
    for i in range(1 << 12):
        arr_number = 0
        arr_sum = 0
        for j in range(12):
            # 자리를 하나씩 비트연산으로 왼쪽으로 옮기면서 1이 있을 경우 갯수와 합을 더해 저장합니다.
            if i & (1 << j):
                arr_number += 1
                arr_sum += j+1
        # 조건문을 돌면서 원소의 갯수가 N개이고 부분집합의 합이 K인 조건을 만족하면
        # result에 1을 더하고 다음 반복문을 실행 합니다.
        if arr_number == N and arr_sum == K:
            result += 1
        # 아닐경우 다음 반복문을 실행합니다.
        else:
            continue

    # 만약 합이 조건과 일치할경우 1 아닐경우 0을 출력 합니다.
    print(f'#{t} {result}')