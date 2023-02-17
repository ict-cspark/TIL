# Baekjoon Online Judge - 회문

import sys
input = sys.stdin.readline


def palindrome(words):
    times = len(words) // 2

    for t in range(times):
        if words[t] != words[-t - 1]:
            return t
    else:
        return -1


T = int(input())

for _ in range(T):
    words = list(input().strip())
    t = palindrome(words)
    if t == -1:
        print(0)
    else:
        rt = len(words) - t - 1
        words_left = words[:t] + words[t + 1:]
        words_right = words[:rt] + words[rt + 1:]

        t_left = palindrome(words_left)
        if t_left == -1:
            print(1)
        else:
            t_right = palindrome(words_right)
            if t_right == -1:
                print(1)
            else:
                print(2)
