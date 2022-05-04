# Baekjoon Online Judge - 나무 자르기

'''
상근이는 환경에 매우 관심이 많기 때문에,
나무를 필요한 만큼만 집으로 가져가려고 한다.
이때, 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.
'''


import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

trees.sort(reverse=True)                    # trees 리스트를 내림차순으로 정렬

start = 1                                   # 이진탐색으로 위한 시작값으로 1 대입
end = trees[0]                              # 끝값으로 trees[0] 대입

while start <= end:                         # start가 end보다 같거나 작을때까지 반복문 실행
    answer = 0                              # 잘린 나무 양 저장을 위한 answer 변수 생성
    mid = (start + end) // 2                # mid에 start + end를 2로 나눈 몫을 저장
    for tree in trees:                      # trees의 요소를 불러와
        if tree > mid:                      # 만약 tree가 mid 보다 더 크다면
            answer += (tree - mid)          # answer에 tree - mid 의 차이를 저장
        else:
            break                           # 아닐 경우 반복문 종료

    if answer >= M:                         # 만약 answer가 M보다 같거나 크다면
        start = mid + 1                     # 시작지점을 mid + 1로 설정
    else:
        end = mid - 1                       # 아닐경우 종료지점을 mid - 1로 설정

print(end)                                  # end 값 출력