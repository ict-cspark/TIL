import sys
sys.stdin = open("input.txt", "r")

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    num = list(map(str, input().split()))
    n_stack = []                        # 숫자를 저장할 빈 스택 리스트 생성
    result = 0

    for n in num:
        if n.isdecimal():               # n이 숫자일 경우 n_stack에 n값을 int로 변환해 push
            n_stack.append(int(n))

        else:
            if n == '.':                # n이 '.'일 경우 아래 조건문 수행
                if len(n_stack) > 1:    # n_stack의 길이가 1이상일 경우
                    result = 'error'    # error 를 result에 저장하고 break
                    break
            else:
                if len(n_stack) >= 2:   # len을 이용하여 길이가 2 이상일 경우에만 아래 조건문 실행
                    n2 = n_stack.pop()  # n2와 n1에 pop을 하여 각각 저장
                    n1 = n_stack.pop()
                    if n == '+':        # n이 +,-,*,/ 중에 하나 일경우 아래 4개의 조건문에 각각 실행
                        result = n1 + n2
                        n_stack.append(result)      # n_stack에 result값 추가
                    elif n == '-':
                        result = n1 - n2
                        n_stack.append(result)
                    elif n == '*':
                        result = int(n1 * n2)
                        n_stack.append(result)
                    elif n == '/':                  # 나눗셈은 // 을이용하여 몫을 구하거나 결과값을 int로 변환
                        result = int(n1 / n2)
                        n_stack.append(result)

                else:                               # 그외 모든경우는 error로 저장
                    result = 'error'
                    break

    print(f'#{test_case} {result}')                 # result 결과값을 출력