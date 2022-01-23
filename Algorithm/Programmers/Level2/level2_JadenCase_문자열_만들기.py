# Programmers - Level2 - JadenCase 문자열 만들기

'''
JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.
'''

def solution(s):
    ss = s.lower()
    lst = ss.split(' ')
    tlst = []
    for i in lst:
        if i != '':
            tlst.append(i)
    result = list(map(lambda x: x[0].upper() + x[1:],tlst))
    answer = ' '.join(result)
    return answer