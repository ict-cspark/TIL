# Programmers - Level3 - 정수 삼각형

def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            left = 0
            right = 0
            if 0 <= j - 1:
                left = triangle[i - 1][j - 1]
            if j < len(triangle[i - 1]):
                right = triangle[i - 1][j]

            triangle[i][j] += max(left, right)

    answer = max(triangle[-1])
    return answer