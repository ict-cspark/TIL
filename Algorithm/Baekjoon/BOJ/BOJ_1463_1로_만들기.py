# Baekjoon Online Judge - 1로 만들기

'''
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.
'''

# 점화식 : D[N] = min(D[N/3] + 1, D[N/2] + 1, D[N-1] + 1)

N = int(input())

memory = [0] * 1000001                  # 메모리 저장을 위한 리스트 생성

for n in range(2, N + 1):               # 1로 나누어떨어지는 수를 구하므로 2부터 N까지 반복문 실행
    memory[n] = memory[n - 1] + 1       # 우선적으로 memory[n]에 memory[n-1]에 1을 더한 값을 저장

    if n % 2 == 0:                      # 만약 n이 2로 나누어떨어질 경우
        # 현재위치의 저장된 값과 n//2로 나눈 인덱스의 값에 1을 더한 값 중 최솟값 저장
        memory[n] = min(memory[n], memory[n // 2] + 1)

    if n % 3 == 0:                      # 만약 n이 3로 나누어떨어질 경우
        # 현재위치의 저장된 값과 n//2로 나눈 인덱스의 값에 1을 더한 값 중 최솟값 저장
        memory[n] = min(memory[n], memory[n // 3] + 1)

print(memory[N])                        # 메모리N에 저장된 값 출력