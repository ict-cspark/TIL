# Baekjoon Online Judge - 수 묶기

'''
수열이 주어졌을 때, 수열의 각 수를 적절히 묶었을 때, 그 합이 최대가 되게 하는 프로그램을 작성하시오.
'''

N = int(input())                                # 수열크기 N 입력 받기
num = [int(input()) for _ in range(N)]          # 수열 입력받아 num 리스트에 저장

plus = []                                       # 2이상 수를 저장할 plus 리스트 생성
minus = []                                      # 음수를 저장할 minus 리스트 생성
one = 0                                         # 1의 갯수를 저장하기 위한 one 변수 생성
zero = 0                                        # 0의 갯수를 저장하기 위핸 zero 변수 생성

for n in num:                                   # num 크기만큼 반복문을 돌면서
    if n > 1:                                   # n이 1보다 클 경우 plus 리스트에 추가
        plus.append(n)
    elif n == 1:                                # n이 1일 경우 one에 1을 더함
        one += 1
    elif n == 0:                                # n이 0일 경우 zero에 1을 더함
        zero += 1
    else:                                       # 음수일 경우 minus에 리스트 추가
        minus.append(n)

plus.sort(reverse=True)                         # plus 리스트 오름차순으로 정렬
minus.sort()                                    # minus 리스트 내림차순으로 정렬

result = 0                                      # 결과저장하기 위한 result 변수 생성
while plus:                                     # plus가 비어있을때까지 반복문 실행
    if len(plus) > 1:                           # plus의 길이가 1보다 크다면
        a = plus.pop(0)
        b = plus.pop(0)
        result += a * b                         # 앞에서부터 두번 pop하여 곱한 뒤 result에 저장
    else:
        a = plus.pop(0)
        result += a                             # 1개만 남아있을 경우 result에 바로 저장

while minus:                                    # minus가 비어있을때까지 반복문 실행
    if len(minus) > 1:                          # minus의 길이가 1보다 크다면
        a = minus.pop(0)
        b = minus.pop(0)
        result += a * b                         # 앞에서부터 두번 pop하여 곱한 뒤 result에 저장
    else:
        a = minus.pop(0)                        # 1개만 남아있을 경우 일단 pop을 한다음
        if zero == 0:                           # 만약 0이 없을 경우에는 result에 a를 더하고 0이 있을 경우 continue
            result += a

result += one                                   # 마지막으로 result에 1의 갯수를 더함

print(result)                                   # 결과값 출력