# Baekjoon Online Judge - 부분 문자열

import sys
input = sys.stdin.readline

while True:
    try:
        s, t = map(str, input().split())

        s_len = len(s)
        start = 0
        for c in t:
            if start == s_len:
                break

            if c == s[start]:
                start += 1
                continue

        if start == s_len:
            print("Yes")
        else:
            print("No")

    except ValueError:
        break
