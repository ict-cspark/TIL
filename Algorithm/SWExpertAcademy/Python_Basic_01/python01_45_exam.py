# 파이썬 기초(1) 45차시 9. 내장함수 - 연습문제 1

# Q. 다음의 결과와 같이 이름과 나이를 입력 받아
# 올해를 기준으로 100세가 되는 해를 표시하는 코드를 작성하십시오.

name = input()
age = int(input())

hundred = 2020 - (age+1) + 100

print('{0}(은)는 {1}년에 100세가 될 것입니다.'.format(name,hundred))