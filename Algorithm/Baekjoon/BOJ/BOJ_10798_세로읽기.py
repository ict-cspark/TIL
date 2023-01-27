# Baekjoon Online Judge - 세로읽기

words = [[False] * 15 for _ in range(5)]

for i in range(5):
    word = str(input())
    for j in range(len(word)):
        words[i][j] = word[j]

result = ""
for c in range(15):
    for r in range(5):
        if words[r][c]:
            result += words[r][c]

print(result)
