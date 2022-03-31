# Baekjoon Algorithm 2단계 If문 - 주사위 세개

'''
1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.
같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.
예를 들어, 3개의 눈 3, 3, 6이 주어지면 상금은 1,000+3×100으로 계산되어 1,300원을 받게 된다.
또 3개의 눈이 2, 2, 2로 주어지면 10,000+2×1,000 으로 계산되어 12,000원을 받게 된다.
3개의 눈이 6, 2, 5로 주어지면 그중 가장 큰 값이 6이므로 6×100으로 계산되어 600원을 상금으로 받게 된다.
3개 주사위의 나온 눈이 주어질 때, 상금을 계산하는 프로그램을 작성 하시오.
'''

number = list(map(int, input().split()))
check = list(set(number))                   # 중복값 확인을 위한 set을 이용

result = 0
if len(check) == 1:                         # check의 갯수가 1개일 경우 3개 모두 같으므로
    result = 10000 + (check[0] * 1000)

elif len(check) == 2:                       # check의 갯수가 2개일 경우 2개가 같으므로
    if number.count(check[0]) == 2:         # 만약 check 첫번째 원소의 값이 number의 2개 있을 경우
        result = 1000 + (check[0] * 100)
    else:                                   # 아닐경우 check의 두번째 원소가 number에서 2개가 있으므로
        result = 1000 + (check[1] * 100)

elif len(check) == 3:                       # check의 갯수가 3개일 경우 3개 모두 다르므로
    result = max(number) * 100

print(result)