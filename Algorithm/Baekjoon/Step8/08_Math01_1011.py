# Baekjoon Algorithm 8단계 Math01 - Fly me to the Alpha Centauri

'''
김우현은 공간이동 장치 작동시의 에너지 소모가 크다는 점을 잘 알고 있기 때문에 x지점에서 y지점을 향해 최소한의 작동 횟수로 이동하려 한다. 
하지만 y지점에 도착해서도 공간 이동장치의 안전성을 위하여 y지점에 도착하기 바로 직전의 이동거리는 반드시 1광년으로 하려 한다.
김우현을 위해 x지점부터 정확히 y지점으로 이동하는데 필요한 공간 이동 장치 작동 횟수의 최솟값을 구하는 프로그램을 작성하라.
'''

T = int(input())

for i in range(T):
    x, y = map(int, input().split(' '))
    
    z = y - x  # y-x의 값을 z에 저장
    result = 0 # 종료 조건 판단을 위해 result 변수 선언
    move = 1 # 이동한 횟수 저장을 위해 move 변수 선언
    count = 0 # move 변수 값이 몇 번 반복하는지 저장을 위해 count 변수 선언
    while z > result: # result 값이 z보다 같거나 커질 경우 반복문 종료
        count += 1 # count 변수에 1을 더하기
        for i in range(2): # 같은 횟수를 두번씩 반복
            result += count # result에 현재 반복 횟수를 더함
            if result >= z: # 만약 result 값이 z보다 같거나 커질 경우 반복문 종료
                break
            move += 1 # 반복횟수를 result에 더할 때마다 이동 횟수 1씩 증가
    print(move) # while 문 종료될 경우 현재 작동횟수 출력