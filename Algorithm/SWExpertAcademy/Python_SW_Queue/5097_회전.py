import sys
sys.stdin = open("input.txt", "r")

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))   # 수열들을 리스트에 저장

    index = M%N                             # 맨 앞에 있는 숫자를 출력하기 위해 M에서 N으로 나눈 나머지를 index에 저장
    
    # 수열에서 맨 앞을 가리키는 수는 수열 리스트에서 M%N으로 구한 값의 인덱스의 값과 일치하므로 reuslt에 해당 인덱스의 값을 저장
    result = num[index]     

    print(f'#{test_case} {result}')         # 결과값 출력