# Baekjoon Online Judge - 회의실 배정

'''
한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 
각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 
단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 
회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.
'''

# 테스트케이스 입력받기
T = int(input())

# 회의시간들을 담을 빈 리스트 생성
time = []
# 반복문을 돌면서 회의시간을 2차원 리스트로 저장
for test_case in range(T):
    time += [list(map(int, input().split()))]

# 저장된 time 리스트에서 종료시간을 기준으로 정렬
# 종료시간이 같을 경우 시작시간을 기준으로 정렬
time.sort(key=lambda x: (x[1], x[0]))

# 0 인덱스에 저장된 회의시간부터 시작하므로
# result와 idx에 1을 저장
# 종료시간을 비교할 변수에 time[0][1]의 값을 초기값을 설정
result = 1
idx = 1
idx_time = time[0][1]
# 인덱스가 테스트케이스보다 작을 때까지만 반복 실행
while idx < T:
    # 만약 시작시간이 idx_time에 저장된 종료시간보다 클경우
    if time[idx][0] >= idx_time:
        # 해당 인덱스의 종료시간을 time에 저장
        idx_time = time[idx][1]
        # result와 idx에 1을 추가
        result += 1
        idx += 1
    # 아닐경우에도 idx에 1을 추가
    else:
        idx += 1

# 결과값 출력
print(result)