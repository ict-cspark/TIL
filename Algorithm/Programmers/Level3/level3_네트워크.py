# Programmers - Level3 - 네트워크


def solution(n, computers):
    answer = 0
    visited = [0] * n
    queue = []
    for i in range(n):
        if visited[i] == 0:
            answer += 1
            visited[i] = 1
            queue.append(i)
            while queue:
                r = queue.pop(0)
                for c in range(n):
                    if visited[c] == 0 and computers[r][c] == 1:
                        queue.append(c)
                        visited[c] = 1

    return answer
