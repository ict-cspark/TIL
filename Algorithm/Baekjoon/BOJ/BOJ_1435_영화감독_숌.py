# Baekjoon Online Judge - 영화감독 숌

N = int(input())
count = 0
number = 666

while count < N:
    if "666" in str(number):
        count += 1
    number += 1

print(number - 1)
