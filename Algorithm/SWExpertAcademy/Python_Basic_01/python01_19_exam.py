# 파이썬 기초(1) 19차시 6. 흐름과 제어 - If - 연습문제 7

# Q. 100~300 사이의 숫자에서 각각의 자리 숫자가 짝수인 숫자를 찾아 콤마(,)로 구분해 출력하는 프로그램을 작성하십시오.

num = list(range(100,301,2))
trans = list(map(str,num))
result = ''
for i in trans:
    if int(i[0])%2 == 0 and int(i[1])%2 == 0 and int(i[2])%2 == 0:
        result += i
        result += ','
print(result[:-1])