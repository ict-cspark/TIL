# 파이썬 기초(1) 11차시 5. 연산자 - 연습문제 5

# Q. 20% 농도의 소금물 100g과 물 200g을 혼합한 소금물의 농도(%)를 소수점 두 번째 자리까지 구하는 프로그램을 작성하십시오.

salt = float(20 / 100 * 100)
water = float(100 - salt)
result = float(salt/(salt+water+200)) * 100
print('혼합된 소금물의 농도: {0:.2f}%'.format(result))