# 1206. [S/W 문제해결 기본] 1일차 - View

'''
강변에 빌딩들이 옆으로 빽빽하게 밀집한 지역이 있다.

이곳에서는 빌딩들이 너무 좌우로 밀집하여, 강에 대한 조망은 모든 세대에서 좋지만 왼쪽 또는 오른쪽 창문을 열었을 때 바로 앞에 옆 건물이 보이는 경우가 허다하였다.

그래서 이 지역에서는 왼쪽과 오른쪽으로 창문을 열었을 때, 양쪽 모두 거리 2 이상의 공간이 확보될 때 조망권이 확보된다고 말한다.

빌딩들에 대한 정보가 주어질 때, 조망권이 확보된 세대의 수를 반환하는 프로그램을 작성하시오.
'''

import sys
sys.stdin = open('input.txt', 'r')

T = 10

for i in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    
    result = 0
    max_lst = []
    for j in range(2,N-2):
        if lst[j] > lst[j-1] and lst[j] > lst[j-2] and lst[j] > lst[j+1] and lst[j] > lst[j+2]:
            max_lst = [lst[j-2], lst[j-1], lst[j+1], lst[j+2]]
            temp = max_lst[0]
            for k in range(4):
                if temp <= max_lst[k]:
                    temp = max_lst[k]
            result += (lst[j] - temp)
        else:
            continue
    print(f'#{i} {result}')