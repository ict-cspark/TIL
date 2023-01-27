# Baekjoon Online Judge - 문자열 게임 2

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    alphabet = {
        "a": [], "b": [], "c": [], "d": [], "e": [], "f": [], "g": [], "h": [], "i": [],
        "j": [], "k": [], "l": [], "m": [], "n": [], "o": [], "p": [], "q": [], "r": [],
        "s": [], "t": [], "u": [], "v": [], "w": [], "x": [], "y": [], "z": []
    }

    W = str(input().strip())
    K = int(input())

    for i in range(len(W)):
        alphabet[W[i]].append(i)

    max_w = 0
    min_w = float("INF")
    for a in alphabet.values():
        if len(a) >= K:
            for j in range(len(a) - K + 1):
                temp = a[j + K - 1] - a[j]
                if temp > max_w:
                    max_w = temp
                if temp < min_w:
                    min_w = temp

    if max_w == 0 and min_w == float("INF"):
        print(-1)
    else:
        print(min_w + 1, max_w + 1)
