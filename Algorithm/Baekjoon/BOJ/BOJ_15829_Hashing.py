# Baekjoon Online Judge - Hashing

L = int(input())
word = input()

result = 0
for i in range(L):
    result += ((ord(word[i]) - 96) * pow(31, i))

print(result % 1234567891)