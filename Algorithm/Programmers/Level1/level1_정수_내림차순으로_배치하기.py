# Programmers - Level1 - 정수 내림차순으로 배치하기

'''
함수 solution은 정수 n을 매개변수로 입력받습니다. 
n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 
예를들어 n이 118372면 873211을 리턴하면 됩니다.
'''

def solution(n):
    answer = 0
    sol=[] 
    while True:
        sol += [n%10]
        if n < 10:
            break
        n = int(n/10)
    sol.sort(reverse=True)
    for i in sol:
        answer+=i
        answer*=10
    answer/=10
    return answer