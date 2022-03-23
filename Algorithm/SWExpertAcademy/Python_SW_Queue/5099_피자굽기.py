import sys
sys.stdin = open("input.txt", "r")

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())            # 화덕 크기 N과 피자 갯수 M 입력 받기
    cheeze = list(map(int, input().split()))    # 치즈의 양 저장
    pizza = []                                  # 피자 번호 저장을 위해 pizza 리스트 생성
    for i in range(M):                          # 피자 갯수만큼 반복문 실행
        pizza.append([cheeze[i], i + 1])        # 치즈 양과 피자 번호를 저장

    oven = []                                   # 오븐 리스트 생성
    for _ in range(N):                          # 화덕 크기만큼 반복문 실행
        oven.append(pizza.pop(0))               # 피자리스트에서 앞에서 꺼내와 oven에 추가

    result = 0                                  # 결과값 저장을 위해 result 변수 생성
    while oven:                                 # oven이 비어있지 않을때까지 반복문 실행
        oven[0][0] = oven[0][0] // 2            # 오븐 첫번째의 저장된 치즈양을 꺼내와 2로나눈 몫을 저장
        if oven[0][0] == 0:                     # 오븐 첫번째 요소의 치즈가 0일 경우
            result = oven.pop(0)                # 첫번째 피자를 pop하고 result에 저장
            if pizza:                           # 만약 대기중인 피자가 있을 경우
                oven.append(pizza.pop(0))       # 첫번째 피자를 꺼내와 oven에 추가
        else:                                   # 치즈가 남아있을 경우
            oven.append(oven.pop(0))            # 피자를 꺼내 오븐 맨뒤에 추가

    print(f'#{test_case} {result[1]}')          # result에 저장된 피자 번호를 출력