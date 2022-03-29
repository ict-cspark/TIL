import sys
sys.stdin = open("input.txt", "r")


def BabyGin(number):                                # BabyGin 판단 함수

    for i in range(8):                              # 0~9까지 3개씩 비교하기 위해 8번 반복
        # 만약 순서대로 3개의 숫자를 비교할 때 run이나 triple 일 경우
        if (number[i] and number[i + 1] and number[i + 2]) or (number[i] >= 3 or number[i + 1] >= 3 or number[i + 2] >= 3):
            return 1                                # 1을 리턴

    return 0                                        # 만족하는 값이 없을 경우 0을 리턴


# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    card = list(map(int, input().split()))          # 카드 입력받아 card 리스트에 저장
    N = len(card)                                   # 카드 갯수 N에 저장

    num1 = [0] * 10                                 # 플레이어1의 카드 숫자를 계산하기 위한 num1 리스트 생성
    num2 = [0] * 10                                 # 플레이어2의 카드 숫자를 계산하기 위한 num1 리스트 생성
    result = 0                                      # 승리 결과를 저장하기 위한 result 변수 생성
    for p in range(N):                              # 카드 갯수만큼 반복문 실행
        if p%2 == 0:                                # p가 짝수일 경우
            num1[card[p]] += 1                      # num1[card[p]]에 1을 더함
            result = BabyGin(num1)                  # BabyGin 함수 실행하여 결과 result에 저장

            if result:                              # result에 값이 있을 경우
                break                               # 반복문 종료
        else:                                       # p가 홀수일 경우
            num2[card[p]] += 1                      # num2[card[p]]에 1을 더함
            result = BabyGin(num2)                  # BabyGin 함수 실행하여 결과 result에 저장

            if result:                              # result의 결과가 저장되었을 경우
                result = 2                          # result의 값을 2로 바꿔주고
                break                               # 반복문 종료
    
    print(f'#{test_case} {result}')                 # 결과값 출력