# Programmers - Level1 - 문자열을 정수로 바꾸기

'''
문자열 s를 숫자로 변환한 결과를 반환하는 함수, solution을 완성하세요.
'''

def solution(s):
    ans = 0
    if 1<= len(s) <=5 and s!='0':
        ans = int(s)
    return ans