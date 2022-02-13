# 1208. [S/W 문제해결 기본] 1일차 - Flatten

'''
한 쪽 벽면에 다음과 같이 노란색 상자들이 쌓여 있다.

높은 곳의 상자를 낮은 곳에 옮기는 방식으로 최고점과 최저점의 간격을 줄이는 작업을 평탄화라고 한다.

평탄화를 모두 수행하고 나면, 가장 높은 곳과 가장 낮은 곳의 차이가 최대 1 이내가 된다.

평탄화 작업을 위해서 상자를 옮기는 작업 횟수에 제한이 걸려있을 때, 제한된 횟수만큼 옮기는 작업을 한 후 최고점과 최저점의 차이를 반환하는 프로그램을 작성하시오.
'''

import sys
sys.stdin = open('input.txt', 'r')

def my_sort(num):
    for i in range(100):
        for j in range(100):
            if num[i] < num[j]:
                temp = num[i]
                num[i] = num[j]
                num[j] = temp
    return num

T = 10

for i in range(1, T+1):
    dump = int(input())
    num = list(map(int, input().split()))
    new_num = my_sort(num)
    for j in range(dump):
        new_num[-1] -= 1
        new_num[0] += 1
        new_num = my_sort(new_num)

    print(f'#{i} {new_num[-1] - new_num[0]}')