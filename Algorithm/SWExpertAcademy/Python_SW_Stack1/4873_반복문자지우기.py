import sys
sys.stdin = open("input.txt", "r")

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    s = input()         # 문자열 입력받기
    result = [s[0]]     # 결과값 저장을 위한 리스트를 생성 후 초기값으로 문자열 첫번째 글자 대입
    word = s[1:]        # 값 비교를 위해 입력받은 문자열을 2번째 글자부터 끝까지의 값을 word에 대입
    for w in word:      # word 길이만큼 반복
        if result != [] and w == result[-1]:    # 만약 result가 빈리스트가 아니고 w와 result 리스트 마지막 값이 같으면
            result.pop(-1)      # result에 마지막 값을 pop하기
        else:
            result.append(w)    # 아닐경우에는 result에 w값을 추가하기

    print(f'#{test_case} {len(result)}') # len을 이용하여 result에 길이를 출력