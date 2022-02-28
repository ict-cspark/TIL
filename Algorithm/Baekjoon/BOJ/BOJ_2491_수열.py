# Baekjoon Online Judge - 수열

'''
0에서부터 9까지의 숫자로 이루어진 N개의 숫자가 나열된 수열이 있다. 그 수열 안에서 연속해서 커지거나(같은 것 포함), 혹은 연속해서 작아지는(같은 것 포함) 수열 중 가장 길이가 긴 것을 찾아내어 그 길이를 출력하는 프로그램을 작성하라. 

예를 들어 수열 1, 2, 2, 4, 4, 5, 7, 7, 2 의 경우에는 1 ≤ 2 ≤ 2 ≤ 4 ≤ 4 ≤ 5 ≤ 7 ≤ 7 이 가장 긴 구간이 되므로 그 길이 8을 출력한다. 수열 4, 1, 3, 3, 2, 2, 9, 2, 3 의 경우에는 3 ≥ 3 ≥ 2 ≥ 2 가 가장 긴 구간이 되므로 그 길이 4를 출력한다. 또 1, 5, 3, 6, 4, 7, 1, 3, 2, 9, 5 의 경우에는 연속해서 커지거나 작아지는 수열의 길이가 3 이상인 경우가 없으므로 2를 출력하여야 한다.
'''

def numUp(num):                 # 연속해서 커지는 수열 체크하는 함수
    result = []                 # 연속횟수 저장을 위한 빈 리스트 생성
    count = 1                   # 연속횟수를 세기 위한 변수를 초기값 1로 설정
    for i in range(N - 1):      # 수열 길이 N-1만큼 반복하여 만약 다음숫자가 같거나 크다면 count 1증가
        if num[i] <= num[i + 1]:
            count += 1
        else:                   # 아닐경우 현재 count값을 result 리스트에 저장하고 값을 1로 초기화
            result.append(count)
            count = 1
    result.append(count)        # 마지막 결과값을 저장을 위해 마지막 count 값을 리스트에 추가
    return max(result)          # result에 저장된 리스트 중 최댓값을 return

def numDown(num):               # 연속해서 작아지는 수열 체크하는 함수
    result = []
    count = 1
    for i in range(N - 1):      # 수열 길이 N-1만큼 반복하여 만약 다음숫자가 같거나 작다면 count 1증가
        if num[i] >= num[i + 1]:
            count += 1
        else:
            result.append(count)
            count = 1
    result.append(count)
    return max(result)


# 수열길이 N 입력받기
N = int(input())
num = list(map(int, input().split()))       # 숫자를 입력받아 정수형태로 리스트에 저장

result1 = numUp(num)                        # 올라가는 연속숫자의 최대갯수를 출력하는 함수
result2 = numDown(num)                      # 내려가는 연속숫자의 최대갯수를 출력하는 함수

print(max(result1, result2))                # result1과 result2 중 최댓값을 출력