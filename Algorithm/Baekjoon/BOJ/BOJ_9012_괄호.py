# Baekjoon Online Judge - 괄호

N = int(input())

for _ in range(N):
    PS = input()
    VPS = 0
    for p in PS:
        if p == "(":
            VPS += 1
        else:
            VPS -= 1

        if VPS < 0:
            print("NO")
            break
    else:
        if VPS == 0:
            print("YES")
        else:
            print("NO")
