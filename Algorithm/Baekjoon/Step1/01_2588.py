# Baekjoon Algorithm 1단계 입출력과 사칙연산 - 곱셈

'''
(세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
(1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.
'''

A = input()
B = input()
print(int(A)*int(B[2]))
print(int(A)*int(B[1]))
print(int(A)*int(B[0]))
print(int(A)*int(B))