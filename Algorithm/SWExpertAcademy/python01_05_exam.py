# 파이썬 기초(1) 5차시 4. 변수 - 연습문제

# Q. 1~9 사이의 정수 a를 입력받아 a + aa + aaa + aaaa 의 값을 계산하는 프로그램을 작성하십시오.

x = input()
result = int(x) + int(x+x) + int(x+x+x) + int(x+x+x+x)
print(result)