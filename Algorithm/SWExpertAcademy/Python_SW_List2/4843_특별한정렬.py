# 4843. [파이썬 S/W 문제해결 기본] 2일차 - 특별한 정렬

'''
보통의 정렬은 오름차순이나 내림차순으로 이루어지지만, 이번에는 특별한 정렬을 하려고 한다.

N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.

예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.
 
10 1 9 2 8 3 7 4 6 5

주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오
'''

import sys
sys.stdin = open('input.txt', 'r')

# 테스트 케이스 입력 받기
T = int(input())

for t in range(1, T + 1):
    # 개수 N과 N개의 정수 lst 리스트로 받기
    N = int(input())
    lst = list(map(int, input().split()))
    # 선택 정렬을 이용하여 짝수번째에는 최댓값을 찾고 두번째에는 최솟값을 번갈아 찾는 반복문 만들기
    for i in range(N-1):
        # 짝수번째 인덱스에서 선택정렬을 통해 최댓값 찾기
        if i%2 == 0:
            max_num = 1
            for j in range(i, N):
                if max_num < lst[j]:
                    max_num = lst[j]
                    lst[i], lst[j] = lst[j], lst[i]

        # 홀수번째 인덱스에서 선택정렬을 통해 최솟값 찾기
        else:
            min_num = 100
            for k in range(i, N):
                if min_num > lst[k]:
                    min_num = lst[k]
                    lst[i], lst[k] = lst[k], lst[i]
    
    # 결과값 출력
    print(f'#{t}', end=" ")
    for i in range(10):
        print(lst[i], end=" ")
    print()
