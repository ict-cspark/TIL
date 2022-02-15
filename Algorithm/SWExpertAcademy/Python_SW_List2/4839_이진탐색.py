# 4839. [파이썬 S/W 문제해결 기본] 2일차 - 이진탐색

'''
코딩반 학생들에게 이진 탐색을 설명하던 선생님은 이진탐색을 연습할 수 있는 게임을 시켜 보기로 했다.

짝을 이룬 A, B 두 사람에게 교과서에서 각자 찾을 쪽 번호를 알려주면, 이진 탐색만으로 지정된 페이지를 먼저 펼치는 사람이 이기는 게임이다.
'''

import sys
sys.stdin = open('input.txt', 'r')

# 테스트 케이스 입력 받기
T = int(input())

for t in range(1,T+1):
    # P, Pa, Pb 입력받기
    P, Pa, Pb = map(int, input().split())

    page_lst = [Pa, Pb]
    page_count = []
    # Pa의 탐색 횟수 찾기
    for pages in page_lst:
        start = 1
        end = P
        count = 0
        while start <= end:
            # 중간값 설정 (몫만)
            middle = (start + end)//2
            # 중간값이 pages와 같다면 count에 1을 더하고 break
            if middle == pages:
                count += 1
                break
            # 만약 중간값이 pages보다 크다면 end값을 중간값으로 바꾸고 다시 반복문 실행
            elif middle > pages:
                end = middle
                count += 1
            # 만약 중간값이 pages보다 작다면 start값을 중간값으로 바꾸고 다시 반복문 실행
            else:
                start = middle
                count += 1
        page_count.append(count)

    # 비교하여 승자 출력하기
    if page_count[0] == page_count[1]:
        print(f'#{t} 0')
    elif page_count[0] < page_count[1]:
        print(f'#{t} A')
    else:
        print(f'#{t} B')