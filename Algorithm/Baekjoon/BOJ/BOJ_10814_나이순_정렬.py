import sys

N = int(input())

members = []

for _ in range(N):
    member = list(map(str, sys.stdin.readline().split()))
    member[0] = int(member[0])
    members.append(member)

members = sorted(members, key=lambda x: x[0])

for age, name in members:
    print(age, name)