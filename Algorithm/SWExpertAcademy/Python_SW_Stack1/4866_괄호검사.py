import sys
sys.stdin = open("input.txt", "r")

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    words = input()
    result = []             # 결과값 판단을 위한 빈 리스트 생성
    for w in words:         # words 길이만큼 반복문 실행
        if w == '(' or w == '{':    # 만약 w가 ( 나 { 일경우 result에 추가
            result.append(w)
        elif w == ')' or w == '}':  # 만약 wrk ) 나 } 일 경우 아래 조건문 실행
            if len(result) == 0:    # 만약 result가 빈리스트일 경우 result에 현재 값 추가하고 break
                result.append(w)
                break
            # 만약 w가 ) 일때 result 마지막값이 ( 아니거나 }일 때 마지막이 { 가 아닐경우
            elif (w == ')' and result[-1] != '(') or (w == '}' and result[-1] != '{'):
                result.append(w)        # result에 현재 값 추가하고 break
                break
            else:
                result.pop(-1)          # 모든 반례 만족하지 않을경우 result에서 마지막값 pop

    if len(result) != 0:                # result 리스트에 값이 있을 경우 0 출력
        print(f'#{test_case} 0')
    else:
        print(f'#{test_case} 1')        # result 리스트에 값이 없을 경우 1 출력