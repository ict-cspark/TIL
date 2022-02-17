# 1216. [S/W 문제해결 기본] 3일차 - 회문2

'''
"기러기" 또는 "level" 과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.
주어진 100x100 평면 글자판에서 가로, 세로를 모두 보아 가장 긴 회문의 길이를 구하는 문제이다.
'''

import sys
sys.stdin = open("input.txt", 'r')

# 회문 판별 함수
def palindrome(words):
    # 회문길이를 100부터 1까지 줄여나가면서 반복
    for i in range(100, 0, -1):
        # 행의 길이를 0부터 99까지 반복
        for c in range(100):
            # 인덱스 에러 방지를 위해
            # 한 행에서 반복 횟수를 행의 길이에서 (회문길이 - 1) 만큼의 값만 반복 실행
            for r in range(100 - (i - 1)):
                # 만약 정방향 문자열과 역방향 문자열이 일치할경우 현재 회문길이 i를 return
                if words[c][r:r+i] == words[c][r:r+i][::-1]:
                    return i

# 테스트 케이스 입력 받기

T = 10

for t in range(1, T + 1):
    N = int(input())

    # 입력받은 문자열을 2차원 리스트로 저장하기 위해 빈 리스트 생성
    words_row = []
    words_col = []
    
    # 100번 반복하면서 문자열을 한줄씩 리스트에 분리해 담고 빈 리스트에 추가해 2차원 리스트 생성
    for n in range(100):
        words_row += [list(map(str, input()))]
    # zip 함수를 이용하여 열 방향 리스트 생성
    words_col = list(map(list,zip(*words_row)))

    # 회문 판별 함수 호출
    row_result = palindrome(words_row)
    col_result = palindrome(words_col)

    # return 받은 결과값중 큰값을 출력
    if row_result >= col_result:
        print(f'#{N} {row_result}')
    else:
        print(f'#{N} {col_result}')














