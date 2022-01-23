# Programmers - Level1 - 약수의 개수와 덧셈

'''
두 정수 left와 right가 매개변수로 주어집니다. 
left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.
'''

def solution(left, right):
    answer = 0
    exp = 0
    for i in range(left,right+1):
        answer = answer + i
        for j in range(1,i+1):
            if i == j*j:
                exp = exp + i
                break
    answer = answer - (2*exp)
    return answer