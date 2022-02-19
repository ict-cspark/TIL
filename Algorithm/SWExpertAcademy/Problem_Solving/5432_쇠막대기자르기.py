# 5432. 쇠막대기 자르기

'''
여러 개의 쇠막대기를 레이저로 절단하려고 한다.
효율적인 작업을 위해서 쇠막대기를 아래에서 위로 겹쳐 놓고, 레이저를 위에서 수직으로 발사하여 쇠막대기들을 자른다.
'''

import sys
sys.stdin = open("input.txt", "r")

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    # 막대기와 레이저 배치 표현식 입력받기
    sticks = input()

    # 현재 막대개수를 저장하고 쇠막대기 조각을 저장할 변수 선언
    count = 0
    piece = 0
    
    # sticks에 저장된 문자열을 하나씩 꺼내와 반복
    for i in range(len(sticks)):
        # i가 '(' 일 경우 현재 막대개수에 1을 더함
        if sticks[i] == '(':
            count += 1
        # i가 ')' 일 경우 현재 막대개수에 1을 빼기
        else:
            count -= 1
            # 만약 이전 인덱스에 i가 '('일 경우
            # 레이저임으로 piece에 count 추가
            if sticks[i - 1] == '(':
                piece += count
            # 아닐경우 가장 위에 막대가 조각났으므로 piece에 1 더함
            else:
                piece += 1

    print(f'#{test_case} {piece}')