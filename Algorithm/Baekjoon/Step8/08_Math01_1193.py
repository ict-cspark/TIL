# Programmers - Level8 - 분수찾기

'''
무한히 큰 배열에 다음과 같이 분수들이 적혀있다.
이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.
'''

X = int(input())

last = 0

for i in range(X):
    last += i+1
    if last >= X:
        order = i+1
        break

if order%2 == 0:
    base = order-(last-X)
    result = str(base) + '/' + str((order+1)-base)
else:
    base = 1 + (last-X)
    result = str(base) + '/' + str((order+1)-base)

print(result)