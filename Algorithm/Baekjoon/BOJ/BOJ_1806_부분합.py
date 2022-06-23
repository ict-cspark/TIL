# Baekjoon Online Judge - 부분합

'''
10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다.
이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중,
가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.
'''


import sys
input = sys.stdin.readline

N, S = map(int, input().split())                    # 수열 N과 합 S 입력 받기
numbers = [0] + list(map(int, input().split()))     # 누적합을 이용하기 위해 [0] 을 추가하고 입력받기

for i in range(1, len(numbers)):                    # 1부터 numbers 길이만큼 반복문 실행하여
    numbers[i] += numbers[i - 1]                    # 누적합 리스트로 만들기

start = end = 0                                     # start, end 변수 생성하여 초기값 0으로 설정
answer = len(numbers)                               # answer는 numbers의 길이로 설정

while end < len(numbers) and answer != 1:           # end가 number 길이보다 작고 answer가 1이 아닐 경우 반복문 실행
    if numbers[end] - numbers[start] < S:           # 만약 end - start 의 누적합 차이가 S보다 작을 경우
        end += 1                                    # end 오른쪽으로 이동
    else:                                           # 클경우
        answer = min(answer, end - start)           # answer에 answer와 end - start 의 차 중 작은 값을 answer에 저장
        start += 1                                  # start 오른쪽으로 이동

if answer == len(numbers):                          # answer가 number의 길이와 같다면
    answer = 0                                      # answer을 0으로 변경

print(answer)                                       # 결과값 출력
