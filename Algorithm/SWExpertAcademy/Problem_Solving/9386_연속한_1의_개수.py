# 9386. 연속한 1의 개수

'''
N개의 0과 1로 이루어진 수열에서 연속한 1의 개수 중 최대값을 출력하는 프로그램을 만드시오.
'''

T = int(input())

for t in range(1,T+1):
    N = int(input())
    num = input()

    result = 0
    result_lst = []
    for i in num:
        if i == '1':
            result += 1
        else:
            result_lst.append(result)
            result = 0

    result_lst.append(result)
    result = max(result_lst)

    print(f'#{t} {result}')
