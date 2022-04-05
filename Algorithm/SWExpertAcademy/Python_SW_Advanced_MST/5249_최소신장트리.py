import sys
sys.stdin = open("input.txt", "r")


def Prim(s):                                            # Prim 함수
    INF = 10000                                         # 무한대값을 저장할 변수 생성
    MST = [0] * (V + 1)                                 # 사용한 정점을 확인하기 위한 MST 리스트 생성
    KEY = [INF] * (V + 1)                               # KEY 값 갱신을 위한 KEY 리스트 생성
    KEY[s] = 0                                          # KEY[s] 값을 0 으로 초기화
    for _ in range(V + 1):                              # V + 1 만큼 반복문 실행
        idx = 0                                         # 정점 번호를 저장하기 위한 idx 변수 생성
        min_value = INF                                 # 최솟값 저장을 위한 min_value 생성
        for i in range(V + 1):                          # V + 1 만큼 반복문 실행
            if MST[i] == 0 and KEY[i] < min_value:      # 방문한 적이 없고 KEY[i] 값이 min_value 보다 작으면
                idx = i                                 # idx와 min_value 값 갱신
                min_value = KEY[i]

        MST[idx] = 1                                    # 방문 흔적을 남기고
        for n, w in adjL[idx]:                          # adjL[idx] 값을 불러와
            if MST[n] == 0 and KEY[n] > w:              # 방문한적이 없는 정점이고 w의 값이 기존에 저장된 키값보다 작다면
                KEY[n] = w                              # 값 갱신

    return sum(KEY)                                     # KEY리스트의 합을 리턴


# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())                    # 마지막 정점 번호와 간선의 갯수 입력 받기
    num = [list(map(int, input().split())) for _ in range(E)]   # 그래프 정보 입력받아 num 리스트에 저장
    adjL = [[] for _ in range(E)]                       # 연결리스트를 사용하기 위한 adjL 생성

    for n1, n2, w in num:                               # num리스트에서 n1, n2, w를 꺼내와
        adjL[n1].append((n2, w))                        # 무방향을 고려하여 연결리스트에 값 추가
        adjL[n2].append((n1, w))

    result = Prim(0)                                    # Prim 함수 호출하여 리턴 값 result에 저장
    print(f'#{test_case} {result}')                     # 결과값 출력