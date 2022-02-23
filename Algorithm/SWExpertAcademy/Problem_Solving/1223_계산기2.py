# 1223. [S/W 문제해결 기본] 6일차 - 계산기2

'''
문자열로 이루어진 계산식이 주어질 때, 이 계산식을 후위 표기식으로 바꾸어 계산하는 프로그램을 작성하시오.
'''

import sys
sys.stdin = open("input.txt", "r")

# 테스트케이스 입력받기
T = 10

for test_case in range(1, T + 1):
    N = int(input())
    num = input()

    pri = {'+': 1,'*': 2} # 연산자 우선순위

    st_num = []             # 숫자가 담길 빈 스택리스트 생성
    st_oper = []            # 연산자가 담길 빈 스택리스트 생성
    for i in range(N):
        if num[i].isdecimal():      # num[i]의 요소가 숫자일 경우 st_num에 추가
            st_num.append(int(num[i]))

        elif st_oper != []:         # st_oper가 빈리스트가 아닐경우 아래 조건문 실행
                                    # st_num의 길이가 2 이상이고 들어올 연산자 우선순위가 작거나 같을 경우
                                    # 위 조건을 만족하지 않을 때까지 반복문 실행
            while st_oper != [] and len(st_num) >= 2 and pri[num[i]] <= pri[st_oper[-1]]:
                p2 = st_num.pop()   # 숫자가 담긴 스택에서 pop을하여 p2에 저장
                p1 = st_num.pop()   # 한번 더 숫자가 담긴 스택에서 pop을하여 p1에 저장
                if pri[st_oper[-1]] == 2:   # 연산자가 담긴 스택의 마지막 요소를 우선순위 딕셔너리와 비교후
                    st_num.append(p1 * p2)  # 2일 경우 p1과 p2 곱을 실행
                    st_oper.pop()           # 해당 연산자 pop
                else:
                    st_num.append(p1 + p2)  # 1일 경우 p1과 p2 합을 실행
                    st_oper.pop()           # 해당 연산자 pop
            st_oper.append(num[i])          # 반복문을 빠져나올 경우 대기중인 연산자를 st_oper에 push
        else:                       # st_oper가 빈리스트일 경우 num[i]요소 스택에 추가
            st_oper.append(num[i])

    while st_oper:                  # 반복문을 빠져나오고 연산자 스택에 요소가 남아있을경우 아래 반복문 실행
        p2 = st_num.pop()           # 내용은 위의 while 반복문과 동일
        p1 = st_num.pop()
        if pri[st_oper[-1]] == 2:
            st_num.append(p1 * p2)
            st_oper.pop()
        else:
            st_num.append(p1 + p2)
            st_oper.pop()

    print(f'#{test_case} {st_num[0]}')
