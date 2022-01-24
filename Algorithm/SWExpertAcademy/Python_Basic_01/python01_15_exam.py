# 파이썬 기초(1) 15차시 6. 흐름과 제어 - If - 연습문제 3

# Q. 다음의 결과와 같이 입력된 영어 알파벳 문자에 대해 대소문자를 구분하는 코드를 작성하십시오.

alph = 'b'
result = ord(alph)
if result >= 65 and result <= 90:
    print('{0} 는 대문자 입니다.'.format(alph))
elif result >=97 and result <=122:
    print('{0} 는 소문자 입니다.'.format(alph))