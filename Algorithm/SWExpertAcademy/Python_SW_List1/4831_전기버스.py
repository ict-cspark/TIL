# 4831. [파이썬 S/W 문제해결 기본] 1일차 - 전기버스

'''
A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.

버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.

충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.

만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.
'''

import sys
sys.stdin = open('input.txt', 'r')

# 노선 수 입력 받고 반복문 생성 (T)
T = int(input())

for i in range(1, T+1):
    # 1회 이동거리 K, 마지막 정류장 번호 N, 충전기 설치 수 M 입력 받기
    K, N, M = map(int, input().split())

    # 충전기 설치 정류장 번호 입력 받고 리스트에 저장
    charge = list(map(int, input().split()))

    # (N+1) 범위를 가진 리스트 생성후 충전기 설치 정류장은 값을 1로 변경
    busstop = [0] * (N+1)
    for j in charge:
        busstop[j] = 1

    # 버스가 이동한 거리와 충전횟수를 저장하기 위한 변수를 선언합니다.
    move = 0
    result = 0
    while result != -1:
        move += K   # 버스가 1회 이동가능한 최대값을 이동합니다.
        if move >= N:   # 만약 이동거리가 마지막 정류장보다 크다면 반복문을 종료합니다.
            break
        if busstop[move] == 1:  # 만약 이동한 정류장에 충전기가 있을 경우
            result += 1         # 충전횟수를 1회 더합니다.
        else:
            for k in range(K):
                if busstop[move] == 1:
                    result += 1
                    break
                elif k == K-1:
                    result = -1
                    break
                else:
                    move -= 1

    if result == -1:
        result = 0
    print(f'#{i} {result}')