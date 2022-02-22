# 1234. [S/W 문제해결 기본] 10일차 - 비밀번호

'''
평소에 잔머리가 발달하고 게으른 철수는 비밀번호를 기억하는 것이 너무 귀찮았습니다.

적어서 가지고 다니고 싶지만 누가 볼까봐 걱정입니다. 한가지 생각을 해냅니다.
 
0~9로 이루어진 번호 문자열에서 같은 번호로 붙어있는 쌍들을 소거하고 남은 번호를 비밀번호로 만드는 것입니다.

번호 쌍이 소거되고 소거된 번호 쌍의 좌우 번호가 같은 번호이면 또 소거 할 수 있습니다.

예를 들어 아래의 번호 열을 철수의 방법으로 소거하고 알아낸 비밀 번호입니다.
'''

import sys
sys.stdin = open("input.txt", "r")

# 테스트케이스 입력받기
T = 10

for test_case in range(1, T + 1):
    N, PWD = map(str, input().split())              # 자리수 N과 번호 문자열을 문자열 형태로 입력받기
    result = [PWD[0]]                               # result에 PWD 첫글자를 초기값으로 설정
    password = PWD[1:]                              # 두번째 부터 마지막 글자까지 password에 대입
    for p in password:                              # password 글자수만큼 반복문 실행
        if len(result) != 0 and p == result[-1]:    # 만약 result가 빈 리스트가 아니고 p와 result 마지막 값이 같을 경우
            result.pop(-1)                          # result 리스트 마지막 값을 pop
        else:
            result.append(p)                        # 아닐경우 result에 p값을 추가

    print(f'#{test_case} {"".join(result)}')        # join 을 이용하여 리스트내에 값을 문자열로 출력
