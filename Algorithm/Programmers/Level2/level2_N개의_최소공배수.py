# Programmers - Level2 - N개의 최소공배수

'''
두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다. 예를 들어 2와 7의 최소공배수는 14가 됩니다. 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다. n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.
'''

def max_num(a,b):
    c = max(a,b)
    for i in range(1,c+1):
        if a%i == 0 and b%i == 0:
            answer = i
    return answer

def solution(arr):
    result = []
    LCM = arr[0]
    for i in range(len(arr)-1):
        GCD = max_num(int(LCM),arr[i+1])
        LCM= LCM*arr[i+1]/GCD
        result.append(LCM)
    answer = int(max(result))
    return answer