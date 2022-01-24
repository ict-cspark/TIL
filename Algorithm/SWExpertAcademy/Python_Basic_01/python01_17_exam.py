# 파이썬 기초(1) 17차시 6. 흐름과 제어 - If - 연습문제 5

# Q. 다음의 결과와 같이 입력된 문자가 대문자일 경우 소문자로, 소문자일 경우 대문자로 변경하고,
# 알파벳이 아닐 경우엔 그냥 출력하는 코드를 작성하십시오.
# 출력 시 아스키코드를 함께 출력합니다.

x = input()
trans = ord(x)

if trans >=65 and trans <=90:
    temp = trans + 32
    print('{0}(ASCII: {1}) => {2}(ASCII: {3})'.format(x,trans,chr(temp),temp))
elif trans >=97 and trans <=122:
    temp = trans - 32
    print('{0}(ASCII: {1}) => {2}(ASCII: {3})'.format(x,trans,chr(temp),temp))
else:
    print(x)