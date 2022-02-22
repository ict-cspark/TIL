# 6485. 삼성시의 버스 노선

'''
삼성시에 있는 5,000개의 버스 정류장은 관리의 편의를 위해 1에서 5,000까지 번호가 붙어 있다.

그리고 버스 노선은 N개가 있는데, i번째 버스 노선은 번호가 Ai이상이고,

Bi이하인 모든 정류장만을 다니는 버스 노선이다.

P개의 버스 정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지 구하는 프로그램을 작성하라.
'''

import sys
sys.stdin = open("input.txt", "r")

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    # 버스노선 수 N 입력 받기
    N = int(input())
    # 버스 정류장 1~5000이 담긴 리스트 생성
    busstop = [0] * 5001
    for n in range(N):
        A, B = map(int, input().split())
        # A부터 B까지 반복을 하면서
        # busstop 리스트의 인덱스와 일치하는 곳에 1을 추가 
        for stop in range(A, B + 1):
            busstop[stop] += 1

    # 출력할 정류장의 갯수 입력받기
    P = int(input())
    print(f'#{test_case}', end=" ")
    # P까지 반복문을 돌면서 출력할 정류장 번호 C를 입력받기
    # 정류장번호의 인덱스와 일치하는 busstop을 출력하여 지나간 버스 횟수를 출력
    for p in range(P):
        C = int(input())
        print(busstop[C], end=" ")
    print()