# 5789. 현주의 상자 바꾸기

'''
현주는 1번부터 N번까지 N개의 상자를 가지고 있다. 각 상자에는 숫자를 새길 수 있는데 처음에는 모두 0으로 적혀있다.
숫자가 너무 단조로웠던 현주는 다음 Q회 동안 일정 범위의 연속한 상자를 동일한 숫자로 변경하려고 한다. 변경하는 방법은 다음과 같다.
   ·  i (1 ≤ i ≤ Q)번째 작업에 대해 L번 상자부터 R번 상자까지의 값을 i로 변경
현주가 Q회 동안 위의 작업을 순서대로 한 다음 N개의 상자에 적혀있는 값들을 순서대로 출력하는 프로그램을 작성하라.
'''

import sys
sys.stdin = open("input.txt", "r")

# 테스트케이스 입력 받기
T = int(input())
for test_case in range(1, T + 1):
    # 리스트 길이 N과 반복횟수 Q 입력받기
    N, Q = map(int, input().split())

    # 0으로 채워진 길이 N 리스트 생성
    arr = [0] * N

    # Q 만큼 반복문을 실행하여 L, R 입력받기
    for i in range(1, Q + 1):
        L, R = map(int, input().split())

        # L ~ R 인덱스 만큼 arr 리스트에 i로 채우기
        for j in range(L - 1, R):
            arr[j] = i

    # 결과를 문자열로 출력
    result = " ".join(map(str, arr))
    print(f'#{test_case} {result}')