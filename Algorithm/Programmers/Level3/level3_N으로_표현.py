# Programmers - Level3 - N으로 표현

def solution(N, number):
    dp = []                             # dp 리스트 생성
    for i in range(1, 9):               # 반복문을 8번 실행 하여 N으로 구성된 초기 set이 담긴 리스트 생성
        dp.append(set([int(str(N)*i)]))

    for i in range(8):                  # 8번 반복문 실행
        for j in range(i):
            for x in dp[j]:             # dp[j]의 원소 갯수만큼 반복문 실행
                for y in dp[i-j-1]:     # dp[i-j-1] 의 원소갯수만큼 반복문 실행
                    dp[i].add(x+y)      # 4칙연산 수행하여 dp[i] 에 추가
                    dp[i].add(x-y)
                    dp[i].add(x*y)
                    if y != 0:
                        dp[i].add(x//y)

        if number in dp[i]:             # dp[i]에 number 값이 있을 경우 i + 1 을 리턴
            return i + 1
    return -1
