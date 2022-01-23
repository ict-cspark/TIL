# Programmers - Level2 - 가장 큰 정사각형 찾기

'''
1와 0로 채워진 표(board)가 있습니다. 표 1칸은 1 x 1 의 정사각형으로 이루어져 있습니다. 표에서 1로 이루어진 가장 큰 정사각형을 찾아 넓이를 return 하는 solution 함수를 완성해 주세요. (단, 정사각형이란 축에 평행한 정사각형을 말합니다.)

예를 들어

1	2	3	4
0	1	1	1
1	1	1	1
1	1	1	1
0	0	1	0
가 있다면 가장 큰 정사각형은

1	2	3	4
0	1	1	1
1	1	1	1
1	1	1	1
0	0	1	0
가 되며 넓이는 9가 되므로 9를 반환해 주면 됩니다.
'''

def solution(board):
    score = 0
    
    for i in range(len(board)):
        if 1 in board[i] and score == 0:
            score = 1
        if i == 0:
            continue

        for j in range(1,len(board[0])):
            if board[i][j] != 0:
                board[i][j] += min(board[i-1][j-1],board[i-1][j],board[i][j-1])
            if board[i][j] > score:
                score = board[i][j]

    answer = pow(score,2)
    return answer