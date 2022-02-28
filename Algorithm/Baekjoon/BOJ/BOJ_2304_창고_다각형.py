# Baekjoon Online Judge - 창고 다각형

'''
창고 주인은 창고 다각형의 면적이 가장 작은 창고를 만들기를 원한다. 그림 1에서 창고 다각형의 면적은 98 ㎡이고, 이 경우가 가장 작은 창고 다각형이다.
기둥들의 위치와 높이가 주어질 때, 가장 작은 창고 다각형의 면적을 구하는 프로그램을 작성하시오.
'''

# 기둥 갯수 N개 입력 받기
N = int(input())

column = [tuple(map(int, input().split())) for _ in range(N)]       # 기둥 위치와 높이를 입력받아 튜플형태로 리스트에 각각 저장
column.sort()                                   # 효율적인 수행을 위해 기둥 위치를 기준으로 오름차순으로 정렬

length = column[-1][0]                          # 높이 리스트를 만들기 위해 column에 저장된 가장 먼 위치를 length에 저장
area = [0] * (length + 1)                       # 위치와 높이 값을 대응하기 위해 length 값을 이용하여 area 리스트 생성


for i in range(N):                              # 기둥 갯수만큼 반복문 실행하여 위치에 해당하는 인덱스에 기둥 높이 저장
    area[column[i][0]] = column[i][1]

max_idx = area.index(max(area))                 # 최대 높이가 있는 기둥 위치를 기준으로 양방향으로 조사하기 위해
                                                # 최대 높이가 있는 위치의 인덱스를 max_idx에 저장
result = 0
max_column = 0                                  # 면적을 저장하기 위한 result와 최대 높이를 저장하기 위한 max_column 변수 생성
for s in range(0, max_idx + 1):                 # 처음부터 가장 높은 기둥이 있는 위치까지 반복문 실행
    if area[s] > max_column:                    # 기둥의 높이가 max_column에 저장된 값보다 크다면
        max_column = area[s]                    # 값을 변경하고 result에 해당 면적 더함
        result += max_column
    else:                                       # 아닐경우 기존 max값을 result에 더함
        result += max_column

max_column = 0                                  # 역방향 조사를 위해 max값 초기화
for rs in range(length, max_idx, -1):           # 끝에서부터 가장 큰 높이의 기둥 전까지 반복문 역으로 실행
    if area[rs] > max_column:
        max_column = area[rs]
        result += max_column
    else:
        result += max_column

print(result)                                   # 결과값 출력