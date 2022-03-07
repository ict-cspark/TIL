# Baekjoon Online Judge - 순열 사이클

'''
Figure 1에 나와있는 것 처럼, 순열 그래프 (3, 2, 7, 8, 1, 4, 5, 6) 에는 총 3개의 사이클이 있다. 이러한 사이클을 "순열 사이클" 이라고 한다.
N개의 정수로 이루어진 순열이 주어졌을 때, 순열 사이클의 개수를 구하는 프로그램을 작성하시오.
'''

T = int(input())
for _ in range(T):
    N = int(input())
    num = list(map(int, input().split()))   # 리스트로 입력받아 저장
    num.insert(0, 0)                        # 인덱스를 맞추기 위해 0번째 인덱스에 0 추가
    check = [0] * (N + 1)                   # 체크리스트 생성
    
    count = 0                               # 결과값 저장을 위한 count 변수 생성
    for i in range(1, N + 1):               # 1부터 N + 1까지 반복문 실행
        if check[i] == 1:                   # check[i]가 1일 경우 다음 반복문 실행
            continue
                           
        while check[num[i]] != 1:           # check[num[i]]이 1이 될 때까지 반복문 실행
            check[num[i]] = 1               # check[num[i]]에 1을 대입하고
            i = num[i]                      # i 값을 num[i] 값으로 변경
        count += 1                          # while문 빠져나올경우 count에 1추가

    print(count)                            # 결과값 출력