import sys
sys.stdin = open('input.txt', 'r')

# 테스트 케이스 입력 받기
T = int(input())

for t in range(1, T + 1):
    # 줄 개수 N과 회문 길이 M 입력받기
    N, M = map(int, input().split())
    # NxN 길이를 가진 글자판 입력받아 2차원 행렬로 만들기
    letters = []
    for n in range(N):
        letters += [list(map(str, input()))]

    # N 줄 크기만큼 반복
    for i in range(N):
        result_start = ''
        result_end = ''
        result = ''

        # 행과 열을 반복
        for cr in range(2):
            # 한 줄에서 회문 길이를 뺀 만큼만 반복
            for j in range(N - (M - 1)):

                # 회문 길이의 절반 만큼만 반복
                for k in range(M//2):
                    # 행 탐색
                    if cr == 0:
                        # M의 길이가 홀수일 경우
                        if M % 2 == 1:
                            temp = letters[i][j + (M//2)]
                        # 시작값과 끝값의 인덱스를 지정
                        letter_start = letters[i][j + k]
                        letter_end = letters[i][(j + k + (M - 1)) - (2*k)]
                    # 열 탐색
                    else:
                        # M의 길이가 홀수일 경우
                        if M % 2 == 1:
                            temp = letters[j + (M//2)][i]
                        letter_start = letters[j + k][i]
                        letter_end = letters[(j + k + (M - 1)) - (2*k)][i]

                    # 첫글자와 마지막 글자가 같을 경우
                    if letter_start == letter_end:
                        # 값을 각각 저장
                        result_start += letter_start
                        result_end = letter_end + result_end
                    # 없을 경우 결과 값을 초기화 하고 반복문 종료
                    else:
                        result_start = ''
                        result_end = ''
                        break
                # 결과 값이 있을 경우 result에 결과 값을 합치기
                # M이 홀수일 경우 중간에 temp 삽입
                if result_start != ''and result_end != '' and M % 2:
                    result = result_start + temp + result_end
                    break
                # 아닐 경우 start와 end만 합치기
                else:
                    result = result_start + result_end

            # 행탐색 중에 result에 결과값이 있을 경우 열탐색 하지않고 break
            if result != '':
                break

        # result에 결과값이 있을 경우 더이상 N줄을 탐색하지 않고 결과값 출력
        if result != '':
            print(f'#{t} {result}')
            break