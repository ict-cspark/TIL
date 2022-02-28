# Baekjoon Online Judge - 빙고

'''
0철수는 친구들과 빙고 게임을 하고 있다.
철수가 빙고판에 쓴 수들과 사회자가 부르는 수의 순서가 주어질 때,
사회자가 몇 번째 수를 부른 후 철수가 "빙고"를 외치게 되는지를 출력하는 프로그램을 작성하시오.
'''

def diag(bingo):                # 빙고에서 양쪽 대각선을 저장하여 리턴하는 함수
    result = []                 # 결과값 저장을 위한 리스트 생성
    for i in range(2):          # 양쪽 대각선을 저장하기 위해 2번 반복
        temp = []               # 대각선 요소 저장을 위한 임시 리스트 생성
        for j in range(5):      # 한 줄의 원소 저장을 위해 5번 반복
            # 정방향, 역방향 대각선을 위해 열의 값 j 뒤에  i*(4*i - 2*j) 추가 (i가 1일 때만 실행)
            temp.append(bingo[j][j + i*(4*i - 2*j)])
        result.append(temp)     # temp리스트를 result에 추가
    return result               # result를 리턴

def row(bingo):                 # 열에서 빙고를 검색하기 위해 열방향으로 2차원리스트를 저장하여 반환하는 함수
    result = list(map(list, zip(*bingo)))   # map과 zip 함수 이용
    return result

def check(number):              # 빙고를 하나씩 부를때마다 사용자의 빙고판에 0으로 체크하는 함수
    for r in range(5):
        for c in range(5):
            if user[r][c] == number:    # user[r][c]가 사회자가 부른 number와 일치하면 0으로 바꾼 후 함수 종료
                user[r][c] = 0
                return

user = [list(map(int, input().split())) for _ in range(5)] # 사용자의 빙고판을 user 리스트에 생성
mc = []     # 사회자의 빙고 순서를 5줄로 받는 입력을 1차원리스트에 25개의 원소로 변경하여 대입
for _ in range(5):
    mc += list(map(int, input().split()))


for i in range(25):     # 25번 반복문 실행
    check(mc[i])        # check 함수를 실행하여 빙고판에 해당 숫자를 찾아 0으로 교체

    bingo = 0           # 빙고횟수를 찾기 위해 0으로 초기화
    user_D = diag(user) # 대각선 원소를 저장하는 함수를 불러와 user_D에 저장
    user_R = row(user)  # 열방향으로 원소를 저장하는 함수를 불러와 usder_R에 저장
    for d in range(2):  # 대각선 횟수만큼 반복하여 한 줄에 0이 다섯개일 경우 빙고에 1을 추가
        if user_D[d].count(0) == 5:
            bingo += 1
    for rc in range(5): # 행과 열을 탐색하기 위해 다섯번 반복문 실행하여 한 줄에 0이 다섯개일경우 빙고에 1을 추가
        if user[rc].count(0) == 5:
            bingo += 1
        if user_R[rc].count(0) == 5:
            bingo += 1

    if bingo >= 3:      # 만약 빙고가 3이상일 경우 result에 인덱스를 고려하여 1을 추가하고 반복문 종료
        result = i + 1
        break

print(result)           # result를 출력