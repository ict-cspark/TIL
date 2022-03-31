# 1865. 동철이의 일 분배

'''
동철이가 차린 전자회사에는 N명의 직원이 있다.
그런데 어느 날 해야할 일이 N개가 생겼다.
동철이는 직원들에게 공평하게 일을 하나씩 배분하려고 한다.
직원들의 번호가 1부터 N까지 매겨져 있고, 해야 할 일에도 번호가 1부터 N까지 매겨져 있을 때, i번 직원이 j번 일을 하면 성공할 확률이 Pi, j이다.
여기서 우리는 동철이가 모든 일이 잘 풀리도록 도와주어야 한다.
직원들에게 해야 할 일을 하나씩 배분하는 방법은 여러 가지다.
우리는 여러 방법 중에서 생길 수 있는 “주어진 일이 모두 성공할 확률”의 최댓값을 구하는 프로그램을 작성해야 한다.
'''

import sys
sys.stdin = open("input.txt", "r")

def DFS(k, S):                                          # DFS 함수 호출, 시작값 k와 확률 합 S
    global result                                       # result 변수 global로 호출

    if result >= S:                                     # result보다 S가 같거나 작다면 함수 종료
        return

    if k == N:                                          # k와 N이 같다면
        if result < S:                                  # result보다 S가 크다면
            result = S                                  # result에 S로 갱신 후 함수 종료
        return
    
    else:                                               # k와 N이 같지 않다면          
        for i in range(N):                              # N 크기만큼 반복문 실행
            if check[i] == 0:                           # check[i] 의 값이 0이라면
                check[i] = 1                            # 1로 값을 변경하고
                DFS(k + 1, S * (member[k][i]/100))      # DFS 함수 호출 (k + 1, S * (member[k][i]/100))
                check[i] = 0                            # 사용흔적 다시 0으로 변경


# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())                                    # 해야할 일 갯수 입력받아 N의 저장
    member = [list(map(int, input().split())) for _ in range(N)]    # 사원마다의 일의 확률 각각 입력받아 member 리스트에 저장

    result = 0                                          # 결과를 저장하기 위한 result 변수 생성
    check = [0] * N                                     # 순열을 만들기 위해 사용흔적을 확인하기 위한 check 리스트 생성
    DFS(0, 1)                                           # DFS 함수 호출

    print(f'#{test_case} {(result * 100):.6f}')         # 결과값 출력