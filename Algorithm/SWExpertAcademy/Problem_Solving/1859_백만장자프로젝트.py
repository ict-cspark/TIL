# 1859. 백만 장자 프로젝트

'''
25년 간의 수행 끝에 원재는 미래를 보는 능력을 갖게 되었다. 이 능력으로 원재는 사재기를 하려고 한다.

다만 당국의 감시가 심해 한 번에 많은 양을 사재기 할 수 없다.

다음과 같은 조건 하에서 사재기를 하여 최대한의 이득을 얻도록 도와주자.

    1. 원재는 연속된 N일 동안의 물건의 매매가를 예측하여 알고 있다.
    2. 당국의 감시망에 걸리지 않기 위해 하루에 최대 1만큼 구입할 수 있다.
    3. 판매는 얼마든지 할 수 있다.

예를 들어 3일 동안의 매매가가 1, 2, 3 이라면 처음 두 날에 원료를 구매하여 마지막 날에 팔면 3의 이익을 얻을 수 있다.
'''

import sys
sys.stdin = open("input.txt", "r")

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    # 날짜 N 입력받고 매매가는 리스트로 변환해서 입력받기
    N = int(input())
    arr = list(map(int, input().split()))

    # 최댓값 비교를 위해 변수 선언 후 arr 배열 가장 마지막 값 대입
    # 이익 저장을 위한 result 변수 생성
    arr_max = arr[N - 1]
    result = 0

    # arr 배열을 역으로 반복
    for i in range(N - 2, -1, -1):
        # 만약 현재 인덱스 위치의 값보다 arr_max값이 크다면
        # result에 arr_max에서 arr[i]값을 빼서 이익을 저장
        if arr_max > arr[i]:
            result += arr_max - arr[i]
        # 만약 arr[i]가 더 크다면 max값을 변경
        else:
            arr_max = arr[i]

    # 결과값 출력
    print(f'#{test_case} {result}')
