# Programmers - Level2 - 프렌즈4블록

'''
블라인드 공채를 통과한 신입 사원 라이언은 신규 게임 개발 업무를 맡게 되었다. 이번에 출시할 게임 제목은 "프렌즈4블록".
같은 모양의 카카오프렌즈 블록이 2×2 형태로 4개가 붙어있을 경우 사라지면서 점수를 얻는 게임이다.

입력으로 블록의 첫 배치가 주어졌을 때, 지워지는 블록은 모두 몇 개인지 판단하는 프로그램을 제작하라.
'''

def solution(m, n, board):
    friends = []                                # 문자열로 받는 board를 분리하기 위한 friends 리스트 생성
    for b in board:                             
        friends.append(list(b))

    answer = 0                                  # 결과값 저장을 위한 answer 변수
    while True:                                 # 종료 조건 만날 때 까지 반복문 실행

        cnt = 0                                 # 2x2 블록의 갯수를 세기 위한 변수 생성
        visited = [[0] * n for _ in range(m)]   # 지울 수 있는 블록을 표시하기 위한 visited 리스트 생성
        for r in range(m - 1):                  # 완전탐색 시작
            for c in range(n - 1):
                # 만약 friends[r][c]에 블록이 존재하고 현재 위치를 기준으로 4개의 블록이 같을 경우
                if friends[r][c] != '' and friends[r][c] == friends[r + 1][c] == friends[r][c + 1] == friends[r + 1][c + 1]:
                    # visited 리스트에 표시하기
                    visited[r][c], visited[r + 1][c],  visited[r][c + 1],  visited[r + 1][c + 1] = 1, 1, 1, 1
                    cnt += 1                    # 지울 수 있는 블록을 찾았기 때문에 cnt에 + 1

        if cnt == 0:                            # 지울수 있는 블록을 하나도 못찾았을 경우 반복문 종료
            break                               # 종료 조건

        for i in range(m):                      # visited 리스트를 탐색하면서 1이 있을 경우
            for j in range(n):
                if visited[i][j] == 1:
                    friends[i][j] = ''          # 프렌즈 블록을 지우고 answer에 1을 추가
                    answer += 1

        for i in range(m - 1, 0, -1):           # 아래서부터 맨 윗줄을 제외하고 탐색 시작
            for j in range(n):
                if friends[i][j] == '':         # 만약 현재 블록이 공백일 경우
                    start = i - 1               # 해당 위치 바로 윗줄을 start로 설정
                    while start >= 0:           # start가 맨 윗줄까지만 반복문 실행
                        if friends[start][j] != '': # 이동하는 위치가 공백이 아닐경우
                            # 서로 위치 교환 후 반복문 종료
                            friends[i][j], friends[start][j] = friends[start][j], friends[i][j]
                            break
                        else:                   # 공백일 경우 윗줄로 이동
                            start -= 1

    return answer                               # 결과 출력


x = solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])
print(x)