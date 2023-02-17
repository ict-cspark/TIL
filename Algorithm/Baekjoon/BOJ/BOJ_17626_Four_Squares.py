# Baekjoon Online Judge - Four Squares

def square(n):
    square_1 = n**0.5
    if int(square_1) == square_1:
        return 1

    for i in range(1, int(n**0.5) + 1):
        square_2 = (n - i**2)**0.5
        if int(square_2) == square_2:
            return 2

    for i in range(1, int(n**0.5) + 1):
        for j in range(1, int((n - i**2)**0.5) + 1):
            square_3 = (n - i**2 - j**2)**0.5
            if int(square_3) == square_3:
                return 3

    return 4


N = int(input())
print(square(N))