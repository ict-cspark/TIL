# Baekjoon Online Judge - 대소문자 바꾸기

word = list(input())

result = ""
for w in word:
    if w.isupper():
        result += w.lower()
    else:
        result += w.upper()

print(result)