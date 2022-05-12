# Programmers - Level2 - JadenCase 문자열 만들기

'''
JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.
'''

def solution(s):
    answer = []                         # 결과값 저장을 위한 answer 리스트 생성
    s = s.lower()                       # s를 소문자로 변환 후저장
    words = s.split(' ')                # s에 공백 한칸을 기준으로 분리하여 words리스트에 저장
    for word in words:                  # words 길이만큼 반복문 실행
        if word == '':                  # 만약 word가 공백이라면
            answer.append(word)         # answer에 바로 추가
        elif word[0].isdecimal():       # word[0] 가 숫자형이라면
            answer.append(word)         # answer에 바로 추가
        else:
            word = word.capitalize()    # word에 첫글자를 대문자로 변경
            answer.append(word)         # answer에 추가

    answer = ' '.join(answer)           # answr리스트를 공백 한칸을 두고 join
    return answer                       # 결과값 출력
