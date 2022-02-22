# 2005. 파스칼의 삼각형

'''
크기가 N인 파스칼의 삼각형을 만들어야 한다.

파스칼의 삼각형이란 아래와 같은 규칙을 따른다.

1. 첫 번째 줄은 항상 숫자 1이다.

2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성된다.
'''

import sys
sys.stdin = open("input.txt", "r")

# pascal 재귀함수 생성
def pascal(N):
    # N이 1일 경우 [1]을 num에 저장하고 return
    if N == 1:
        num = [1]
        return num

    # num에 pascal(N -1) 값을 저장
    num = pascal(N - 1)
    # my_num을 [1]로 초기화
    my_num = [1]

    # 1부터 N까지 반복문 실행
    for i in range(1, N):
        # 값 추가를 위한 임시변수 생성
        temp = 0
        # 만약 i - 1이 0보다 같거나 크다면
        # temp에 num[i - 1] 값을 더함
        if i - 1 >= 0:
            temp += num[i - 1]
        # 만약 i가 N - 1보다 작다면
        # temp에 num[i]값을 더함
        if i < N - 1:
            temp += num[i]
        # my_num리스트에 temp값 추가
        my_num.append(temp)

    # my_num을 리턴
    return my_num

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    # 리스트로 받은 결과값을 join 함수와
    # map, str을 이용하여 출력
    print(f'#{test_case}')
    for n in range(1, N + 1):
        print(" ".join(map(str, pascal(n))))

