import sys
sys.stdin = open("input.txt", "r")

# 암호코드 정보
code = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())                # 배열 크기 N, M 입력받기
    arr = [input() for _ in range(N)]               # 암호코드 정보를 입력받아 arr 배열에 저장

    result = 0                                      # 결과값 출력을 위한 result 변수 생성
    for r in range(N):                              # 행 길이 만큼 반복문 실행
        pwd = arr[r]                                # arr[r]의 값을 pwd에 저장
        start = 0                                   # 시작값을 찾기 위한 start 변수 생성
        for c in range(M - 1, -1, -1):              # 열 길이만큼 역으로 탐색
            if pwd[c] == '1':                       # 만약 '1'이 있을 경우 start에 c + 1 값을 저장 후 반복문 종료
                start = c + 1
                break

        password = []                               # 8개의 암호코드를 저장하기 위한 password 리스트 생성
        value = 0                                   # 암호코드를 검증하기 위한 vaule 변수 생성
        if start >= 56:                             # start의 길이가 암호코드보다 길 경우에만 아래 조건문 실행
            check = pwd[start - 56 : start]         # 56자의 암호코드를 잘라 check에 저장
            for i in range(0, 56, 7):               # 암호코드를 8개씩 잘라서 password에 저장
                password.append(code.index(check[i : i+7]))

            for j in range(0, 8, 2):                # 암호코드를 불러와 홀수번째 코드에는 3을 곱한 값을 더하고 
                value += (password[j] * 3)          # 짝수번째와 검증코드는 바로 vaule에 더하기
                value += password[j + 1]
            if value%10 == 0:                       # value가 10의 배수일 경우에 result에 password 리스트 요소 합을 result에 저장
                result = sum(password)
            else:                                   # 아닐경우 result에 0을 저장
                result = 0

    print(f'#{test_case} {result}')                 # result 출력