# 파이썬 기초(1) 8차시 5. 연산자 - 연습문제 2

# Q. 킬로그램(kg)를 파운드(lb)으로 변환하는 프로그램을 작성하십시오.
# 이 때 1 킬로그램은 2.2046 파운드입니다.

x = int(input())
print('{0:.2f} kg =>  {1:.2f} lb'.format(x,x*2.2046))