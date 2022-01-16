# 파이썬 기초(1) 14차시 6. 흐름과 제어 -If - 연습문제 2

# Q. 다음의 결과와 같이 임의의 양의 정수를 입력받아 그 정수의 모든 약수를 구하십시오
# (단, 약수가 2개일 경우 소수임을 나타내십시오)

prime = 0
lst = []
num = int(input())
for i in range(1,num+1):
    if num%i == 0:
        print('{0}(은)는 {1}의 약수입니다.'.format(i,num))
        lst.append(i)
        prime += 1
if prime == 2:
    pass
    print('{0}(은)는 {1}과 {2}로만 나눌 수 있는 소수입니다.'.format(num,lst[0],lst[1]))