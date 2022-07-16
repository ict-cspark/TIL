# Baekjoon Online Judge - 보물

'''
옛날 옛적에 수학이 항상 큰 골칫거리였던 나라가 있었다.
이 나라의 국왕 김지민은 다음과 같은 문제를 내고 큰 상금을 걸었다.
길이가 N인 정수 배열 A와 B가 있다. 다음과 같이 함수 S를 정의하자.
S = A[0] × B[0] + ... + A[N-1] × B[N-1]
S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자.
단, B에 있는 수는 재배열하면 안 된다.
S의 최솟값을 출력하는 프로그램을 작성하시오.
'''


import sys
input = sys.stdin.readline

'''
# 1 정렬 사용

N = int(input())                        # N을 입력받기
A = list(map(int, input().split()))     # N 갯수만큼 입력받아 A 리스트에 저장
B = list(map(int, input().split()))     # N 갯수만큼 입력받아 B 리스트에 저장

A.sort()                                # A를 오름차순으로 정렬
B.sort(reverse=True)                    # B를 내림차순으로 정렬

S = 0                                   # 결과값 출력을 위한 S 변수 생성하여 0으로 초기화
for i in range(N):                      # N만큼 반복문을 실행
    S += A[i] * B[i]                    # S에 A[i] * B[i]의 값을 S에 저장

print(S)                                # 결과값 S 출력
'''

N = int(input())                        # N을 입력받기
A = list(map(int, input().split()))     # N 갯수만큼 입력받아 A 리스트에 저장
B = list(map(int, input().split()))     # N 갯수만큼 입력받아 B 리스트에 저장


S = 0                                   # 결과값 출력을 위한 S 변수 생성하여 0으로 초기화
for i in range(N):                      # N만큼 반복문을 실행
    A_new = A.pop(A.index(min(A)))      # A 리스트의 최솟값의 인덱스를 찾아 pop하여 A_new에 저장
    B_new =  B.pop(B.index(max(B)))     # B 리스트의 최댓값의 인덱스를 찾아 pop하여 B_new에 저장
    S += A_new * B_new                  # S 에 A_new * B_new 값을 더함

print(S)                                # 결과값 S 출력