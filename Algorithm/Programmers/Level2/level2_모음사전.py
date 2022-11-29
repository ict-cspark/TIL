# Programmers - Level2 - 모음사전

from itertools import product

# s1
def solution1(word):
    words = []
    for i in range(1, 6):       # 반복문 실행하여 중복순열 실행
        for c in product(["A", "E", "I", "O", "U"], repeat=i):
            words.append("".join(list(c)))      # words 리스트에 join이용하여 문자열로 추가

    words.sort()                # 알파벳순으로 정렬
    answer = words.index(word) + 1  # index 이용하여 word 찾기

    return answer

# s2
def solution2(word):
    answer = 0
    word_idx = {"A": 0, "E": 1, "I": 2, "O": 3, "U": 4}

    for i in range(len(word)):
        answer += ((5 ** (5 - i) // 4) * word_idx[word[i]] + 1)     # 등비수열 합 공식 이용
    return answer