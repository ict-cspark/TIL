# 4834. [파이썬 S/W 문제해결 기본] 1일차 - 숫자 카드

'''
0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.

가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.
'''

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for i in range(1,T+1):
    N = int(input())
    card = list(map(int,input()))

    count = [0] * 10
    for j in card:
        count[j] += 1

    my_max = 0
    my_index = 0
    for k in range(10):
        if count[k] >= my_max:
            my_max = count[k]
            my_index = k

    print(f'#{i} {my_index} {my_max}')