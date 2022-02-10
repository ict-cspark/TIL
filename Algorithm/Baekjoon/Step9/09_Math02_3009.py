# Baekjoon Algorithm 9단계 Math02 - 네 번째 점

'''
세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.
'''

def my_only(a,b,c):
    if a == b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a

a,x = map(int,input().split())
b,y = map(int,input().split())
c,z = map(int,input().split())

print(my_only(a, b, c), my_only(x, y, z))