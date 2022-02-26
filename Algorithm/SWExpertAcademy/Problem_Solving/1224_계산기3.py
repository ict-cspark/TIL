import sys
sys.stdin = open("input.txt", "r")

# 테스트케이스 입력받기
T = 10

ICP = {'(': 3, '+': 1, '*': 2}      # 들어오는 연산자의 우선순위    
ISP = {'(': 0, '+': 1, '*': 2}      # 스택안에 있는 연산자의 우선순위

op = {                              # lambda 함수를 이용하여 연산을 간편하게 저장
    '+': lambda x,y: x + y,
    '*': lambda x,y: x * y,
}

def convert(calc):
    stack = []                              # 연산기호를 저장할 스택리스트 생성
    result = ''
    for i in calc:                          # calc 길이만큼 반복문 실행
        if i.isdecimal():                   # 만약 숫자형태일 경우에는 result에 추가
            result += i
        elif i == '(':                      # 여는 괄호일 경우 스택에 push
            stack.append(i)
        elif i == ')':                      # 닫는 괄호일 경우 아래 반복문 실행
            while stack != [] and stack[-1] != '(':     # 스택이 빈스택이 아니고 스택 마지막 요소가 여는 괄호가 아닐 때까지
                result += stack.pop()       # result에 스택에서 pop한 요소를 더함
            stack.pop()                     # 여는 괄호를 만나면 해당 요소를 pop
        else:
            while stack != [] and  ICP[i] <= ISP[stack[-1]]:        # 스택이 비어있지 않고 들어올 연산순위가 스택 마지막 요소의 연산순위와 같거나 작다면
                result += stack.pop()       # result에 스택에서 pop한 요소를 더함
            stack.append(i)                 # 스택이 비어있거나 들어올 기호의 연산순위가 크면 스택에 push
    while stack != []:                      # 스택이 비어있지 않다면 result에 스택이 빈 리스트가 될때까지 pop
        result += stack.pop()

    return result                           # result를 반환

def number(num):
    number = []                             # 숫자를 저장할 빈 스택리스트 생성
    for n in num:
        if n.isdecimal():                   # 숫자형태일 경우 int로 변환하여 number 리스트에 pop
            number.append(int(n))
        elif n in op:                       # n이 op 딕셔너리 안에 있을 경우
            n2 = number.pop()               # number 리스트에서 pop을 각각 하여 n2, n1에 저장
            n1 = number.pop()
            number.append(op[n](n1, n2))    # number 리스트에 op 딕셔너러리의 키를 이용하여 연산후 다시 pop
    return number[-1]                       # number 마지막 요소를 반환

for test_case in range(1, T + 1):
    N = int(input())
    calc = input()

    new_calc = convert(calc)            # 후위연산을 수행하는 함수 호출
    result = number(new_calc)           # 후위연산식을 계산하는 함수 호출

    print(f'#{test_case} {result}')