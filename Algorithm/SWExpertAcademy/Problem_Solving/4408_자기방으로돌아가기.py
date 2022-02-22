# 4408. 자기 방으로 돌아가기

'''
모든 학생들은 현재 위치에서 자신의 방으로 돌아가려고 하는데, 만약 두 학생이 자기방으로 돌아가면서 지나는 복도의 구간이 겹치면 두 학생은 동시에 돌아갈 수 없다.

예를 들어 (방1 -> 4) 와 (방3 -> 6) 은 복도 구간이 겹치므로 한 사람은 기다렸다가 다음 차례에 이동해야 한다. 이동하는 데에는 거리에 관계없이 단위 시간이 걸린다고 하자.

각 학생들의 현재 방 위치와 돌아가야 할 방의 위치의 목록이 주어질 때, 최소 몇 단위시간만에 모든 학생들이 이동할 수 있는지를 구하시오.

'''

import sys
sys.stdin = open("input.txt", "r")

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    # 방갯수만큼 0으로 채워진 빈 리스트 생성
    room = [0] * 401
    for _ in range(N):
        A, B = map(int, input().split())
        # 만약 A가 B보다 크다면 값을 서로 교체
        if A > B:
            A, B = B, A
        # 만약 A가 짝수라면 A에 -1을 해주기
        # 방이 양쪽에 있으므로 이를 대응해주기 위해
        if A%2 == 0:
            A = A - 1
        # A와 B범위만큼 room 리스트에 1을 추가
        for i in range(A, B + 1):
            room[i] += 1

    # room 리스트 중에서 가장 큰 값 찾기
    result = 0
    for j in range(401):
        if result < room[j]:
            result = room[j]

    # 결과값 출력
    print(f'#{test_case} {result}')