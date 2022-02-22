import sys
sys.stdin = open("input.txt", "r")

# 테스트케이스 입력받기
T = int(input())

# 규칙 찾기 ex) N : 3일 경우 N이 1일 때의 값 + 2의 N - 1번째 승의 합
for test_case in range(1, T + 1):
    N = int(input()) // 10          # 입력 받은 값을 10으로 나눈 몫을 N으로 저장
    result = [1, 3]                 # result 리스트에 1번째, 2번째 초기값 1, 3을 저장
    for i in range(2, N):           # 반복문을 2부터 시작하여 규칙을 적용하여 리스트에 추가
        result.append(result[i - 2] + (2 ** i))

    # 리스트에 저장된 마지막 값을 결과값으로 출력
    print(f'#{test_case} {result[-1]}')