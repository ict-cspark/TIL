# 파이썬 기초(1) 18차시 6. 흐름과 제어 - If - 연습문제 6

# Q. 1~200 사이의 정수 가운데 7의 배수이면서 5의 배수는 아닌 모든 숫자들을 찾아
# 콤마(,)로 구분된 문자열을 구성해 출력하는 프로그램을 작성하십시오.

num = list(range(1,201))
result = ''
for i in num:
    if i%7 == 0 and i%5 != 0:
        result += str(i)
        result += ','
print(result[:-1])