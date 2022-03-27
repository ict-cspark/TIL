import sys
sys.stdin = open("input.txt", "r")

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N, H = map(str, input().split())            # 자릿수 N과 16진수 H 입력받기

    num = []                                    # 10진수 저장을 위한 num 리스트 생성
    for h in H:                                 # 16진수를 불러와 10진수로 변환후 num 리스트에 저장
        num.append(int(h, 16))

    result = ''                                 # 2진수 저장을 위한 result 변수 생성
    for n in num:                               # 10진수를 불러와 반복문 실행
        result += format(n, 'b').zfill(4)       # 2진수로 변환후 4자리가 아닐시 왼쪽에 0으로 채움

    print(f'#{test_case} {result}')             # 결과값 출력