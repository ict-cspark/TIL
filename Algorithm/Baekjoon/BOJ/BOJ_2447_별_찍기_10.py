# Baekjoon Online Judge - 별 찍기 - 10 

'''
재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.

크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.
'''

def star(x):
    if x == 1:
        return ['*']
    x = x // 3
    a = star(x)
    topbottom = [i * 3 for i in a]
    middle = [i + ' ' * x + i for i in a]
    return topbottom + middle + topbottom

N = int(input())
mystar = '\n'.join(star(N))
print(mystar)