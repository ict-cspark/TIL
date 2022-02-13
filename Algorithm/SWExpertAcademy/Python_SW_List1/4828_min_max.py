# 4828. [파이썬 S/W 문제해결 기본] 1일차 - min max

'''
N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.
'''

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for i in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))

    my_min = num[0]
    my_max = num[0]
    for j in range(N):
        if num[j] <= my_min:
            my_min = num[j]
        if num[j] >= my_max:
            my_max = num[j]

    result = my_max - my_min
    print(f'#{i} {result}')