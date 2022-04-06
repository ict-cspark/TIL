# 5648. [모의 SW 역량테스트] 원자 소멸 시뮬레이션

'''
N 개의 원자들의 [x, y] 위치, 이동 방향, 보유 에너지가 주어질 때 원자들이 소멸되면서 방출하는 에너지의 총합을 구하는 프로그램을 작성하라.
'''

import sys
sys.stdin = open("input.txt", "r")

delta = [(1, 0), (-1, 0), (0, -1), (0, 1)]              # 델타 사용을 위한 리스트 생성 (상, 하, 좌, 우)

# 테스트케이스 입력받기
T = int(input())                                        

for test_case in range(1, T + 1):
    N = int(input())                                    # 원자들의 수 입력받아 N에 저장
    atom = [list(map(int, input().split())) for _ in range(N)]  # 원자들의 정보 입력받아 atom 리스트에 저장
    for i in range(len(atom)):                          # 0.5 이동을 방지하기 위해 원자들의 x, y 값에 곱하기 2를 하여 저장
        atom[i][0] = atom[i][0] * 2
        atom[i][1] = atom[i][1] * 2

    result = 0                                          # 결과값 저장을 위한 result 변수 생성
    for _ in range(4002):                               # -2000 ~ 2000 이동을 위한 반복문 실행
        dd = set()                                      # 가지치기를 위한 방향 저장 set 생성
        for kk in range(len(atom)):                     # atom 리스트를 불러와 반복문 실행
            dd.add(atom[kk][2])                         # atom 리스트의 방향을 저장
        if len(dd) == 1:                                # 만약 dd의 길이가 1이라면
            break                                       # 모두 같은방향이므로 더이상 실행하지 않고 break
        for k in range(len(atom) - 1, -1, -1):          # 인덱스 벗어나는 원자를 찾기위한 가지치기
            if abs(atom[k][0]) > 2000 or abs(atom[k][1]) > 2000:    # atom의 x,y 좌표중 하나라도 절대값이 2000이 넘으면
                atom.pop(k)                             # atom 리스트에서 원자 제거
        for d in range(len(atom)):                      # atom 리스트 길이만큼 반복문 실행하여 방향을 참고하여 x, y값 이동
            atom[d][0] += delta[atom[d][2]][1]          # x 좌표는 열 이동이기 때문에 델타 2번째 값 참고       
            atom[d][1] += delta[atom[d][2]][0]          # y 좌표는 행 이동이기 때문에 델타 첫번째 값 참고

        delete = set()                                  # 삭제하기 위한 set 생성
        visit = set()                                   # 방문흔적을 남기기위한 set 생성
        for n in range(len(atom)):                      # atom 길이만큼 반복문 실행
            nc = atom[n][0]                             # nc에 atom[n][0] 저장
            nr = atom[n][1]                             # nr에 atom[n][1] 저장
            if (nc, nr) in visit:                       # 만약 (nc, nr) 값이 visit에 있다면
                delete.add((nc, nr))                    # delete에 추가
            visit.add((nc, nr))                         # visit 에 (nc, nr) 값 추가

        for j in range(len(atom) - 1, -1, -1):          # 인덱스 에러를 방지하기위해 뒤에서부터 반복문 실행
            if (atom[j][0], atom[j][1]) in delete:      # (atom[j][0], atom[j][1])의 값이 delete에 있다면
                result += atom[j][3]                    # result에 에너지를 더하고
                atom.pop(j)                             # atom리스트에서 j인덱스 값을 pop

        if len(atom) < 2:                               # atom리스트의 길이가 2보다 작다면 반복문 종료
            break

    print(f'#{test_case} {result}')                     # 결과값 출력