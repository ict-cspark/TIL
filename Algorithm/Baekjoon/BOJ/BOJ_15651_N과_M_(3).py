# Baekjoon Online Judge - N과 M (3)

'''
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
1부터 N까지 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
'''

import itertools # 중복순열을 사용하기 위해 itertools를 import

N, M = map(int, input().split())

num = list(range(1, N + 1)) # 1부터 N까지의 리스트 생성
result = list(itertools.product(num , repeat = M)) # num 리스트에스 M개의 원소를 가지는 중복순열 생성하여 result에 저장

for i in result:        # 결과 출력
    print(' '.join(map(str, i)))