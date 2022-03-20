# Baekjoon Online Judge - 크리스마스 선물

'''
크리스마스에는 산타가 착한 아이들에게 선물을 나눠준다. 올해도 산타는 선물을 나눠주기 위해 많은 노력을 하고 있는데,
전세계를 돌아댕기며 착한 아이들에게 선물을 나눠줄 것이다.
하지만 산타의 썰매는 그렇게 크지 않기 때문에, 세계 곳곳에 거점들을 세워 그 곳을 방문하며 선물을 충전해 나갈 것이다.
또한, 착한 아이들을 만날 때마다 자신이 들고있는 가장 가치가 큰 선물 하나를 선물해 줄 것이다.
'''


N = int(input())

gift = []                                       # 선물의 가치를 담기 위한 리스트 생성
for _ in range(N):
    info = list(map(int, input().split()))      # info에 들어오는 숫자들을 저장
    if info[0] == 0:                            # info[0]의 값이 0이면 아래 조건문 실행
        if len(gift) != 0:                      # gift에 값이 있을 경우
            result = max(gift)                  # gift에서 가장 큰 값을 result에 저장
            print(result)                       # result 출력
            gift.remove(result)                 # result를 gift에서 제거
        else:
            print(-1)                           # gift가 비어있을 경우 -1을 출력
    else:                                       # info[0]의 값이 0이 아닐경우
        C = info[0]                             # C에 info[0]의 값을 저장
        for c in range(1, C + 1):               # info 리스트에 1부터 C까지 반복문 실행
            gift.append(info[c])                # gift에 info[c] 값 추가


'''
import heapq                                    # heapq 를 사용하기 위한 import 실행
N = int(input())

heap = []                                       # heap을 저장하기 위한 리스트 생성
for _ in range(N):

    info = list(map(int, input().split()))
    if info[0] == 0:
        if len(heap) != 0:
            result = -(heapq.heappop(heap))     # heappop을 실행하여 가장 작은 값 꺼내와서 양수로 바꿔서 저장
            print(result)
        else:
            print(-1)
    else:
        C = info[0]
        for c in range(1, C + 1):
            heapq.heappush(heap, -(info[c]))    # info[c]의 값을 음수로 바꾸어서 heappush
'''