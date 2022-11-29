# Programmers - Level3 - 단어 변환

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer

    word_len = len(words)
    visited = [0] * word_len
    queue = [begin]

    while queue:
        word = queue.pop(0)

        if word == target:
            answer = visited[words.index(target)]
            break

        for i in range(word_len):
            result = 0
            if visited[i] == 0:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        result += 1
                if result == 1:
                    if word == begin:
                        visited[i] = 1
                    else:
                        visited[i] = visited[words.index(word)] + 1
                    queue.append(words[i])

    return answer