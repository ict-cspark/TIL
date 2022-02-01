# Baekjoon Algorithm 7단계 String - 단어 공부

'''
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
'''

word = input().upper()
word_set = list(set(word))

word_count = []

for i in word_set:
    word_count.append(word.count(i))

if word_count.count(max(word_count)) > 1:
    print('?')
else:
    result = word_count.index(max(word_count))
    print(word_set[result])