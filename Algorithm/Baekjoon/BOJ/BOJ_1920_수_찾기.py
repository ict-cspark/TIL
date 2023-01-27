# Baekjoon Online Judge - 수 찾기

import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
num_dict = {}
for n in num:
    num_dict[n] = 1

M = int(input())
num_find = list(map(int, input().split()))
for f in num_find:
    if f in num_dict:
        print(1)
    else:
        print(0)
