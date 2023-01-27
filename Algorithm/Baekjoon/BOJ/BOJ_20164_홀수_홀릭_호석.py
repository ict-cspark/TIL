# Baekjoon Online Judge - 홀수 홀릭 호석

def count_odd(num):
    cnt_odd = 0

    for n in num:
        if int(n) % 2:
            cnt_odd += 1

    return cnt_odd


def operation(num, cnt):
    global min_v
    global max_v

    s = str(num)
    cnt += count_odd(s)

    if len(s) == 1:
        min_v = min(min_v, cnt)
        max_v = max(max_v, cnt)
        return

    elif len(s) == 2:
        new_num = num // 10 + num % 10
        operation(new_num, cnt)

    else:
        for i in range(1, len(s) - 1):
            for j in range(i + 1, len(s)):
                new_num = int(s[:i]) + int(s[i:j]) + int(s[j:])
                operation(new_num, cnt)


N = int(input())

min_v = float("INF")
max_v = 0

operation(N, 0)

print(min_v, max_v)
