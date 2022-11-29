# Programmers - Level3 - 여행 경로

from collections import defaultdict


def solution(tickets):
    answer = []
    routes = defaultdict(list)
    for start, end in tickets:
        routes[start].append(end)

    for route in routes:
        routes[route].sort(reverse=True)

    stack = ["ICN"]
    while stack:
        plane = stack.pop()
        if plane not in routes or not routes[plane]:
            answer.append(plane)
        else:
            stack.append(plane)
            stack.append(routes[plane].pop())

    return answer[::-1]