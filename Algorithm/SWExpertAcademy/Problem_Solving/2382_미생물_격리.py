# 2382. [모의 SW 역량테스트] 미생물 격리

'''
정사각형 구역 안에 K개의 미생물 군집이 있다.
이 구역은 가로 N개, 세로 N개, 총 N * N 개의 동일한 크기의 정사각형 셀들로 이루어져 있다.
미생물들이 구역을 벗어나는걸 방지하기 위해, 가장 바깥쪽 가장자리 부분에 위치한 셀들에는 특수한 약품이 칠해져 있다.
M 시간 동안 이 미생물 군집들을 격리하였다. M시간 후 남아 있는 미생물 수의 총합을 구하여라.
'''

import sys
sys.stdin = open("input.txt", "r")

delta = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]              # 델타 생성 (상, 하, 좌, 우)
switch = [0, 2, 1, 4, 3]                                        # 방향 전환을 위한 리스트 저장


def move(arr):                                                  # move 함수
    for i in range(len(arr)):                                   # arr 길이만큼 반복문 실행
        arr[i][0] = arr[i][0] + delta[arr[i][3]][0]             # 가로의 값을 저장되어 있는 방향을 반영하여 이동
        arr[i][1] = arr[i][1] + delta[arr[i][3]][1]             # 세로의 값을 저장되어 있는 방향을 반영하여 이동

        if 0 < arr[i][0] < N - 1 and 0 < arr[i][1] < N - 1:     # 만약 미생물의 위치가 약품 셀 안쪽이라면 continue
            continue
        else:                                                   # 약품이 칠해져있는 셀이라면
            arr[i][2] = arr[i][2] // 2                          # 미생물을 반으로 줄이고
            arr[i][3] = switch[arr[i][3]]                       # 방향 전환
    arr.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)    # key=lambda를 이용하여 arr 리스트 내림차순으로 정렬

    start = 1                                                   # 초기값으로 시작 1로 설정
    while start < len(arr):                                     # start가 arr 길이 범위 내일경우만 반복문 실행
        # 만약 현재 미생물의 위치가 바로 앞의 미생물과 일치할 경우
        if arr[start][0] == arr[start - 1][0] and arr[start][1] == arr[start - 1][1]:
            arr[start - 1][2] += arr[start][2]                  # 앞의 미생물에 자신의 미생물 수를 합하고
            arr.pop(start)                                      # 자신은 pop 하여 제거
        else:
            start += 1                                          # 위치가 같지 않을 경우 한칸 이동

    return


# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())                         # 셀의 갯수와 격리 시간, 미생물 갯수 N, M, K 입력받기
    group = [list(map(int, input().split())) for _ in range(K)] # 미생물 정보 입력받아 group 리스트에 저장

    for _ in range(M):                                          # 격리시간만큼 반복문 실행하여 move 함수 호출
        move(group)

    result = 0                                                  # 미생물 총합을 구하기 위한 변수 result 생성
    for g in range(len(group)):                                 # group의 길이만큼 반복문 실행
        result += group[g][2]                                   # result에 미생물 갯수 저장
    print(f'#{test_case} {result}')                             # 결과값 출력