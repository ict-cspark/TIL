# Baekjoon Algorithm 8단계 Math01 - ACM 호텔

'''
ACM 호텔 매니저 지우는 손님이 도착하는 대로 빈 방을 배정하고 있다. 
고객 설문조사에 따르면 손님들은 호텔 정문으로부터 걸어서 가장 짧은 거리에 있는 방을 선호한다고 한다. 
여러분은 지우를 도와 줄 프로그램을 작성하고자 한다. 
즉 설문조사 결과 대로 호텔 정문으로부터 걷는 거리가 가장 짧도록 방을 배정하는 프로그램을 작성하고자 한다.
'''

T = int(input())

for i in range(T):
    H, W, N = map(int, input().split(' '))
    if N%H == 0:
        Y = N//H
        X = H
    else:
        Y = (N//H) + 1
        X = N%H
    
    YY = str(Y).rjust(2, '0')
    result = int(str(X) + YY)
    print(result)

