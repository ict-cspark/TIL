# 1232. [S/W 문제해결 기본] 9일차 - 사칙연산

'''
사칙연산으로 구성되어 있는 식은 이진 트리로 표현할 수 있다. 아래는 식 “(9/(6-4))*3”을 이진 트리로 표현한 것이다.
임의의 정점에 연산자가 있으면 해당 연산자의 왼쪽 서브 트리의 결과와 오른쪽 서브 트리의 결과를 사용해서 해당 연산자를 적용한다.
사칙연산 “+, -, *, /”와 양의 정수로만 구성된 임의의 이진트리가 주어질 때, 이를 계산한 결과를 출력하는 프로그램을 작성하라.
'''

import sys
sys.stdin = open("input.txt", "r")

def ca(first, second, op):                      # 사칙연산을 해주는 함수
    if op == '+':                               # op값을 판단하여 각 조건문을 통해 해당 연산 값을 리턴
        return first + second
    elif op == '-':
        return first - second
    elif op == '*':
        return first * second
    elif op == '/':
        return first / second

def info_type(char):                            # 문자 타입 판단 함수
    if char.isnumeric():                        # 문자가 숫자형태이면 int로 변환하여 리턴하고
        return int(char)
    else:
        return char                             # 아닐경우 그대로 리턴

# 테스트케이스 입력받기
T = 10

for test_case in range(1, T + 1):
    N = int(input())                            # 입력값을 info_type 함수를 이용해 int, char구분하여 저장
    info = [list(map(info_type, input().split())) for _ in range(N)] 

    calc = ['+', '-', '*', '/']                 # 사칙연산을 하기 위한 calc 리스트 생성
    tree = [0] * (N + 1)                        # 트리 리스트를 만들어 인덱스를 일치시키기 위해 N + 1로 생성

    for n in range(N):                          # N만큼 반복문 실행
        t = n + 1                               # 인덱스 일치시키기 위해 t는 n에 1을 더해 저장
        tree[t] = info[n][1]                    # info[n][1]의 값을 tree[t]에 저장

    for t in range(N, 0, -1):                   # 트리를 올라가면서 계산하기 위해 N부터 1까지 역으로 반복문 실행
        if tree[t] in calc:                     # tree[t]의 값이 연산자일 경우
            first = tree[info[t - 1][2]]        # 왼쪽 자식 노드 번호를 찾고 tree에서 값을 구해 first에 저장
            second = tree[info[t - 1][3]]       # 오른쪽 자식 노드 번호를 찾고 tree에서 값을 구해 first에 저장
            op = tree[t]                        # 연산자를 op에 저장
            answer = ca(first, second, op)      # first, second, op값을 이용하여 ca함수를 호출하고 리턴 값을 answer에 저장
            tree[t] = answer                    # tree[t]에 answer 값을 저장

    result = int(tree[1])                       # tree[1]값을 int로 변한하여 result에 저장
    print(f'#{test_case} {result}')             # 결과값 출력