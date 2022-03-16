# 1231. [S/W 문제해결 기본] 9일차 - 중위순회

import sys
sys.stdin = open("input.txt", "r")

def in_order(v):                # 중위순회를 위한 함수
    if v:
        global result           # 값 저장을 위한 global 변수 선언
        in_order(ch1[v])        # 왼쪽 자식정점 값으로 함수 재호출
        result += V_info[v]     # 문자가 저장된 V_info리스트의 인덱스에 위치하는 값을 result에 추가
        in_order(ch2[v])        # 오른쪽 자식정점 값으로 함수 재호출

# 테스트케이스 입력받기
T = 10

for test_case in range(1, T + 1):
    V = int(input())
    info = [list(map(str, input().split())) for _ in range(V)]
    info.insert(0, ['0'])           # 인덱스를 맞추기 위해 앞에 리스트 추가


    V_info = [0] * (V + 1)          # 문자 저장을 위한 리스트 생성
    ch1 = [0] * (V + 1)             # 왼쪽 자식 정점 값 저장을 위한 리스트 생성
    ch2 = [0] * (V + 1)             # 오른쪽 자식 정점 값 저장을 위한 리스트 생성

    for i in range(1, V + 1):       # 정점 길이만큼 반복문 실행
        V_info[i] = info[i][1]      # V_info에 info i번째 행의 두번째 값을 저장
        if len(info[i]) == 3:       # info[i]의 길이가 3이라면
            ch1[i] = int(info[i][2])    # 왼쪽 자식노드에 info[i]행의 세 번째 값을 저장
        elif len(info[i]) == 4:     # info[i]의 길이가 4이라면
            ch1[i] = int(info[i][2])    # 왼쪽 자식노드에 info[i]행의 세 번째 값을 저장
            ch2[i] = int(info[i][3])    # 오른쪽 자식노드에 info[i]행의 네 번째 값을 저장

    result = ''                     # 결과값 저장을 위한 빈 문자열 저장
    in_order(1)                     # 1번 정점부터 시작
    print(f'#{test_case} {result}') # 결과값 출력