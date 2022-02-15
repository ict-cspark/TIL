# 1954. 달팽이 숫자

'''
달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.

다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.
'''

import sys
sys.stdin = open('input.txt', 'r')

# 테스트케이스 입력 받기
T = int(input())

for t in range(1,T+1):
    # 정수 N 입력받고 0으로 채운 N*N 2차원 행렬 만들기
    N = int(input())
    arr = [[0]*N for n in range(N)]

    # 델타를 이용하기 위해 시계 방향으로 배열 생성
    dc = [0, 1, 0, -1]
    dr = [1, 0, -1, 0]
    
    # N**2 만큼 반복문 실행하여 0으로 채워진 행렬에 숫자 채우기
    nc = 0
    nr = 0
    # arr[0][0]은 1로 초기값 설정하고 2부터 반복문 시작
    arr[0][0] = 1
    for i in range(2, (N**2)+1):
        # 델타 행렬을 순차적으로 반복하면서 arr 행렬에 i값을 넣을때까지 종료하지 않고 계속 반복
        while arr[nc][nr] != i:
            # 델타 행렬 길이만큼 반복
            for j in range(4):
                nc += dc[j]
                nr += dr[j]
                # 만약 nc와 nr 값이 arr 행렬 범위 안에 있는지 확인
                if 0 <= nc < N and 0 <= nr < N:
                    # 해당 요소의 값이 0일 경우 i값 대입 후 break
                    if arr[nc][nr] == 0:
                        arr[nc][nr] = i
                        break
                    # 아닐경우 이전으로 되돌리기 위해 값을 다시 빼주고
                    # 델타 리스트 첫번째 요소를 마지막으로 순서 변경 후 break
                    else:
                        nc -= dc[j]
                        nr -= dr[j]
                        temp = dc.pop(0)
                        dc.append(temp)
                        temp = dr.pop(0)
                        dr.append(temp)
                        break

                # 인덱스를 벗어날경우 이전으로 되돌리기 위해 값을 빼주고
                # 델타 리스트 첫번째 요소를 마지막으로 순서 변경 후 break
                else:
                    nc -= dc[j]
                    nr -= dr[j]
                    temp = dc.pop(0)
                    dc.append(temp)
                    temp = dr.pop(0)
                    dr.append(temp)
                    break

    # 결과 출력
    print(f'#{t}')
    for r in range(N):
        for c in range(N):
            print(arr[r][c], end=' ')
        print()