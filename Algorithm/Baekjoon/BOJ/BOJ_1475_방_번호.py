# Baekjoon Online Judge - 방 번호

number = { '0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0 }

N = list(str(input()))

for n in N:
    if n == '9':
        number['6'] += 1
    else:
        number[n] += 1

number['6'] = number['6'] - number['6'] // 2

result = []
for value in number.values():
    result.append(value)

print(max(result))
