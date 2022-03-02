# Programmers - Level2 - 땅따먹기

'''
땅따먹기 게임을 하려고 합니다. 땅따먹기 게임의 땅(land)은 총 N행 4열로 이루어져 있고, 모든 칸에는 점수가 쓰여 있습니다. 1행부터 땅을 밟으며 한 행씩 내려올 때, 각 행의 4칸 중 한 칸만 밟으면서 내려와야 합니다. 단, 땅따먹기 게임에는 한 행씩 내려올 때, 같은 열을 연속해서 밟을 수 없는 특수 규칙이 있습니다.

예를 들면,

| 1 | 2 | 3 | 5 |

| 5 | 6 | 7 | 8 |

| 4 | 3 | 2 | 1 |

로 땅이 주어졌다면, 1행에서 네번째 칸 (5)를 밟았으면, 2행의 네번째 칸 (8)은 밟을 수 없습니다.

마지막 행까지 모두 내려왔을 때, 얻을 수 있는 점수의 최대값을 return하는 solution 함수를 완성해 주세요. 위 예의 경우, 1행의 네번째 칸 (5), 2행의 세번째 칸 (7), 3행의 첫번째 칸 (4) 땅을 밟아 16점이 최고점이 되므로 16을 return 하면 됩니다. 
'''

def solution(land):
    for i in range(len(land)-1):
        land[i+1][0] = max(land[i][1:4]) + land[i+1][0]
        land[i+1][1] = max(land[i][0:1] + land[i][2:4]) + land[i+1][1]
        land[i+1][2] = max(land[i][0:2] + land[i][3:4]) + land[i+1][2]
        land[i+1][3] = max(land[i][0:3]) + land[i+1][3]

    return max(land[-1])

'''
def solution(land):
for i in range(1, len(land)):       # 두 번째 행부터 마지막 행까지 반복문 실행
    for j in range(len(land[0])):   # 한 행의 길이만큼 반복문 실행
        # 이전 행에서 j열 인덱스를 제외하고 리스트를 슬라이싱 한 다음
        # max값을 구하여 현재 요소에 값을 더함
        land[i][j] += max(land[i - 1][ : j] + land[i -1 ][j + 1 :])

# 마지막 행에서 최댓값을 구하여 return
return max(land[-1])
'''