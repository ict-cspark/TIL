# Programmers - Level5 - 최소, 최대

'''
N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
'''

N = int(input())
lst = list(map(int,input().split(' ')))
min = lst[0]
max = lst[0]
for i in range(N):
    if lst[i] >= max:
        max = lst[i]
    if lst[i] <= min:
        min = lst[i]
print(min, max)