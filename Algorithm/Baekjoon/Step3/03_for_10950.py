# Baekjoon Algorithm 3단계 For문 - A+B-3

'''
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
'''

num = int(input())
for i in range(num):
    result = list(map(int, input().split(' ')))
    total = result[0] + result[1] 
    print(total)