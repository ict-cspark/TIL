import sys
sys.stdin = open('input.txt', 'r')

# 테스트 케이스 입력 받기
T = int(input())

for t in range(1, T+1):
    str1 = input()
    str2 = input()

    # str1을 저장할 딕셔너리 생성
    N = dict()

    # str1 문자열을 반복하여 딕셔너리의 키값으로 저장 value 값은 0
    for i in str1:
        N[i] = 0

    # str2 반복문을 돌면서 j값이 N 딕셔너리에 키값으로 있을 경우
    for j in str2:
        if N.get(j) != None:
            # 1을 추가
            N[j] += 1

    # 결과값 저장을 위한 변수 선언
    max_result = 0
    # N의 value 값이 max_result 보다 크면 max_result에 k값 저장
    for k in N.values():
        if max_result < k:
            max_result = k

    # 결과값 출력
    print(f'#{t} {max_result}')