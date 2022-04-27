# Baekjoon Online Judge - 좌표 압축

'''
수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.
Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.
X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.
'''


import sys

N = int(input())
num = list(map(int, sys.stdin.readline().split()))
newNum = sorted(set(num))               # 입력받은 num 리스트의 중복을 제거하고 오름차순으로 정렬

order = {}                              # newNum의 순서와 값을 저장할 order 딕셔너리 생성
result = []                             # num의 값을 저장할 result 리스트 생성
for i in range(len(newNum)):            # newNum 길이만큼 반복문 실행
    order[newNum[i]] = i                # order 딕셔너리에 값과 순서 저장

for j in num:                           # num 리스트의 요소를 불러와
    result.append(order[j])             # result에 order 키에 해당하는 값을 저장

print(*result)                          # result 언패킹하여 출력