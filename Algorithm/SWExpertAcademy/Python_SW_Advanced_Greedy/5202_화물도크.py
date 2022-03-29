import sys
sys.stdin = open("input.txt", "r")

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())                                # 신청서 갯수 N 입력받기
    form = [list(map(int, input().split())) for _ in range(N)]  # 신청서 정보 form 리스트에 저장
    form.sort(key=lambda x: (x[1], x[0]))           # form 리스트를 lambda를 이용하여 오름차순으로 정렬 (우선순위 x[1], x[0)

    result = 1                                      # 첫번째 화물차를 기본값으로 1 대입
    time = form[0][1]                               # 첫번째 화물차의 끝나는시간을 time의 대입
    for i in range(1, N):                           # 두번째 화물차 부터 끝까지 반북문 실행
        if time <= form[i][0]:                      # 만약 time 보다 현재 화물의 시작시간이 같거나 크다면
            result += 1                             # result에 1을 더하고
            time = form[i][1]                       # time의 현재화물 끝나는시간으로 갱신

    print(f'#{test_case} {result}')                 # 결과값 출력