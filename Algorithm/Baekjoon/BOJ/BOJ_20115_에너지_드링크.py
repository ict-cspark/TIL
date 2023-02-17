# Baekjoon Online Judge - 에너지 드링크

N = int(input())
drinks = list(map(int, input().split()))

max_drink = max(drinks)
answer = (sum(drinks) - max_drink) / 2

if answer % 1:
    result = answer + max_drink
else:
    result = int(answer) + max_drink
print(result)
