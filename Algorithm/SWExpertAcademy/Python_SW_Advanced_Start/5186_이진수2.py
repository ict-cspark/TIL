import sys
sys.stdin = open("input.txt", "r")

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N = float(input())                          # 실수 N을 float로 입력 받기

    answer = 0                                  # 값 비교를 위한 answer 변수 생성
    result = ''                                 # 결과 출력을 위한 result 변수 생성
    for i in range(1, 14):                      # 1부터 overflow 판단을 위해 13까지 반복문 실행
        answer += pow(2,-i)                     # answer에 2의 -i승의 값을 answer에 저장
        if N == answer:                         # N과 answer가 일치할 경우
            result += '1'                       # result에 1을 추가하고 반복문 종료
            break
        elif N > answer:                        # N이 answer 보다 클 경우 
            result += '1'                       # result에 1을 추가하고 다음 반복문 실행
        else:                                   # answer가 더 클 경우
            answer -= pow(2, -i)                # answer에서 다시 2의 -i승을 빼주고
            result += '0'                       # result에 0을 추가

    if len(result) > 12:                        # 반복문 종료 후 빠져나온 result의 길이가 12보다 클 경우
        result = 'overflow'                     # result에 overflow를 저장

    print(f'#{test_case} {result}')             # 결과 출력