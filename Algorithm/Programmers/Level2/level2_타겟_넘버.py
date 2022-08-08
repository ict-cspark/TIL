# Programmers - Level2 - 타겟 넘버


def solution(numbers, target):
    answer = 0
    num_len = len(numbers)

    def DFS(N, K):
        nonlocal answer

        if N == num_len:
            if K == target:
                answer += 1
                return

        else:
            DFS(N + 1, K + numbers[N])
            DFS(N + 1, K - numbers[N])

        return

    DFS(0, 0)

    return answer