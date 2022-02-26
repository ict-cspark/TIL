import sys
sys.stdin = open("input.txt", "r")

def password(pwd):          # password 함수
    idx = -1                # idx 값을 -1로 초기화
    while True:             # result를 return 할때까지 반복문 실행
        for i in range(5):  # 5번 반복문 실행
            idx += 1        # idx에 1을 더함
            ni = idx%8      # idx에 8을 나눈 나머지를 ni에 저장
            pwd[ni] -= (i + 1)  # pwd[ni] 값에 1, 2, 3, 4, 5 순으로 값을 빼기
            if pwd[ni] <= 0:    # 만약  pwd[ni] 값이 0보다 같거나 작다면
                pwd[ni] = 0     # 해당 인덱스에 0을 대입하기

                result = pwd[ni + 1 :] + pwd[: ni + 1]  # result를 pwd리스트에서 0보다 작아진 인덱스를 찾아 리스트 재배치
                result = ' '.join(map(str, result))     # join함수를 이용하여 str로 출력
                return result       # result를 리턴

# 테스트케이스 입력받기
T = 10

for test_case in range(1, T + 1):
    N = int(input())
    pwd = list(map(int, input().split()))

    result = password(pwd)                  # password 함수를 호출하고 입력받은 pwd 리스트를 대입

    print(f'#{test_case} {result}')         # 결과값을 return