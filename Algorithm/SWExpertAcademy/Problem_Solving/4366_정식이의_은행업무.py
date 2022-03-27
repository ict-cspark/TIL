import sys
sys.stdin = open("input.txt", "r")


def solve(num2, num3):
    num3 = num3[::-1]                               # 뒤에서부터 비교를 위해 num3[::-1] 로 변경

    for i in range(len(num2)):                      # num2의 길이만큼 반복
        n2 = num2[:]
        n2[i] = (num2[i] + 1) % 2                   # n2[i] 번째 값을 바꿈

        d = 0                                       # 십진수 값 저장을 위한 d 변수 생성
        for j in range(len(n2)):                    # n2 길이만큼 반복
            d = (d * 2) + n2[j]                     # d에 2를 곱하고 n2[j]값을 더해 d에 저장
        answer = d                                  # 결과값 리턴을 위해 answer에 d를 저장

        n3 = []                                     # 3진수를 저장하기 위한 리스트 생성
        while d > 0:                                # d가 0보다 클때까지 반복문 실행
            n3.append(d % 3)                        # d에서 3으로 나눈 나머지를 n3에 추가
            d = d//3                                # d에서 3으로 나눈 몫을 d에 저장

        cnt = abs(len(n3) - len(num3))              # 다른 숫자 갯수를 저장하기위해 cnt를 생성하고 초기값으로 두 수의 길이 차이로 설정
        for k in range(min(len(n3), len(num3))):    # 두 수 중에 길이가 짧은 것을 기준으로 반복문 실행
            if n3[k] != num3[k]:                    # 한 자리씩 비교하면서 다를 경우 cnt에 1추가
                cnt += 1
        if cnt == 1:                                # cnt가 1일경우 answer를 리턴
            return answer

    return False                                    # 답을 찾지 못했을 경우 False를 리턴


# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    num2 = list(map(int, input()))                  # 2진수 입력받아 num2에 저장
    num3 = list(map(int, input()))                  # 3진수 입력받아 num3에 저장

    result = solve(num2, num3)                      # solve 함수 호출하여 num2와 num3에 저장

    print(f'#{test_case} {result}')                 # 결과 출력