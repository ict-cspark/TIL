# Programmers - Level6 - 한수

'''
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 
'''

N = int(input())
count = 99
if N <= 99:
    count = N

for i in range(100,N+1):
    i = str(i)
    if int(i[0]) - int(i[1]) == int(i[1]) - int(i[2]):
        count += 1

print(count)



