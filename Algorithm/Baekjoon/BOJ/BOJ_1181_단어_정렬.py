# Baekjoon Online Judge - 단어 정렬

N = int(input())

words = set()

for _ in range(N):
    word = input()
    words.add(word)

words = sorted(list(words))
result = sorted(words, key=lambda x: len(x))

for r in result:
    print(r)
