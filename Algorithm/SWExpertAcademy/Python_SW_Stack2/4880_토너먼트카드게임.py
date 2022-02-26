import sys
sys.stdin = open("input.txt", "r")

def match(start, end):                  # 그룹을 2로나누는 macth 함수
    if start == end:                    # 만약 시작값과 끝값이 같다면
        return start                    # 시작값을 return (끝값도 상관없음, win 함수 호출때 사용할 값을 위해)
    else:
        left = match(start, (start + end) // 2)     # left는 끝값을 start+end를 2로 나눈 몫으로 설정하도 다시 match 호출
        right = match(((start + end) // 2) + 1, end)    # right는 시작값을 start+end를 2로 나눈 몫에서 1을 더한 값으로 설정하고 match 함수 다시 호출
        return win(left, right)         # win 함수에 left, right 값을 이용하여 호출하고 승자를 return 받기

def win(left, right):                   # 승자 결정 win 함수
    if cards[left] == 1 or cards[right] == 1: # 만약 cards[left], cards[right] 값 중에 1이 있을 경우 아래 조건문 실행
        if cards[left]%3 >= cards[right]%3: # 가위와 보의 승패 판별을 위해 3으로 나눈 나머지로 판별
            return left                     # 왼쪽이 같거나 클경우 left를 return (비길경우에도 편의상 작은 수를 return 하는 규칙)
        else:
            return right                    # 오른쪽이 클 경우 right return
    else:
        if cards[left] >= cards[right]:     # cadrs[left or right] 값이 1이 없을 경우에는 주먹과 보의 승패 판별을 위해 아래 조건문 실행
            return left                     # 왼쪽이 같거나 클경우 left를 return (비길경우에도 편의상 작은 수를 return 하는 규칙)
        else:
            return right                    # 오른쪽이 클 경우 right return

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())                            # 학생 수 N과 카드를 리스트로 입력받기
    cards = list(map(int, input().split()))

    result = match(0, N - 1) + 1                # match 함수에 시작값과 끝값을 포함하여 호출하고
                                                # 인덱스 정보를 받기 때문에 학생번호를 맞추기 위해 1을 더함
    print(f'#{test_case} {result}')