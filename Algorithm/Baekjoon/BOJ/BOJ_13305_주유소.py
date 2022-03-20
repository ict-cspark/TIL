# Baekjoon Online Judge - 주유소

'''
각 도시에 있는 주유소의 기름 가격과,
각 도시를 연결하는 도로의 길이를 입력으로 받아
제일 왼쪽 도시에서 제일 오른쪽 도시로 이동하는
최소의 비용을 계산하는 프로그램을 작성하시오.
'''

N = int(input())
km = list(map(int, input().split()))
city = list(map(int, input().split()))

min_oil = city[0]                       # 최솟값 비교를 위한 변수 생성후 city[0]의 값을 초기값으로 설정
result = city[0] * km[0]                # 결과값 저장을 위한 변수 생성 후 city[0] * km[0]을 초기값으로 설정

ct = len(city)                          # city 리스트의 길이를 ct에 저장
for i in range(1, ct - 1):              # 두번째 인덱스 부터 마지막 인덱스 전까지 반복문 실행
    if min_oil > city[i]:               # city[i]의 값이 min_oil보다 작다면
        min_oil = city[i]               # min_oil에 값을 대입하고
        result += min_oil * km[i]       # result에 min_oil * km[i] 값을 더함
    else:
        result += min_oil * km[i]       # 아닐 경우에는 result에 min_oil * km[i] 값만 더함

print(result)                           # 결과값 출력