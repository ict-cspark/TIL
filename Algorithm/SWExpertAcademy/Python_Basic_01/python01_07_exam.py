# 파이썬 기초(1) 7차시 5. 연산자 - 연습문제

# Q. 인치(inch)를 센티미터(cm)으로 변환하는 프로그램을 작성하십시오.
# 이 때 1 인치는 2.54 센티미터입니다.

x = int(input())
print('{0:.2f} inch => {1:.2f} cm'.format(x,x*2.54))