import sys
sys.stdin = open("input.txt", "r")


def findset(k):                                 # findset 함수 실행
    while k != team[k]:                         # k가 team[k]와 같지 않다면 반복문 실행
        k = team[k]                             # k값 갱신 후 반복문 다시 실행
    return k                                    # 반복문 종료 후 k값 리턴


# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())            # 출석번호와 신청서 갯수 N, M 입력 받기
    num = list(map(int, input().split()))       # 신청서 정보 입력받아 num 리스트에 저장

    team = [i for i in range(N + 1)]            # 자기 번호가 담긴 team 리스트 생성
    for i in range(M):                          # 신청서 갯수만큼 반복문 돌면서
        x = num[i * 2]
        y = num[(i * 2) + 1]
        team[findset(y)] = findset(x)           # findset 함수 실행하여 팀 정보 갱신

    result = 0                                  # 결과값 출력을 위한 result 변수 생성
    for j in range(1, N + 1):                   # 1부터 출석번호 까지 반복문을 돌면서 
        if team[j] == j:                        # 인덱스 번호와 일치하면
            result += 1                         # result에 1을 더함
    print(f'#{test_case} {result}')             # 결과값 출력