# Baekjoon Online Judge - 문자열

T = int(input())

for _ in range(T):
    word = input()
    result = word[0] + word[-1]
    print(result)