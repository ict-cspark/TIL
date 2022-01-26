# 1
'''-----------------------------
print('Hello')
-----------------------------'''

# 2
'''-----------------------------
print('Hello World')
-----------------------------'''

# 3
'''-----------------------------
print('Hello')
print('World')
-----------------------------'''

# 4
'''-----------------------------
print("'Hello'")
-----------------------------'''

# 5
'''-----------------------------
print('"Hello World"')
-----------------------------'''

# 6
'''-----------------------------
print('"!@#$%^&*()\'')
-----------------------------'''

# 7
'''-----------------------------
print('"C:\\Download\\\'hello\'.py"')
-----------------------------'''
# 8
'''-----------------------------
print('print("Hello\\nWorld")')
-----------------------------'''

# 9
'''-----------------------------
a = input()
print(a)
-----------------------------'''

# 10
'''-----------------------------
n = input()
n = int(n)
print(n)
-----------------------------'''

# 11
'''-----------------------------
f = input()
f = float(f)
print(f)
-----------------------------'''

# 12
'''-----------------------------
a = input()
b = input()
print(a)
print(b)
-----------------------------'''

# 13
'''-----------------------------
a = input()
b = input()
print(b)
print(a)
-----------------------------'''

# 14
'''-----------------------------
a = input()
print(a)
print(a)
print(a)
-----------------------------'''

# 15
'''-----------------------------
a,b = input().split()
print(a)
print(b)
-----------------------------'''

# 16
'''-----------------------------
a,b = input().split()
print(b,a)
-----------------------------'''

# 17
'''-----------------------------
a = input()
print(a,a,a)
-----------------------------'''

# 18
'''-----------------------------
a,b = input().split(':')
print(a,b,sep=':')
-----------------------------'''

# 19
'''-----------------------------
a,b,c = input().split('.')
print(c,b,a, sep='-')
-----------------------------'''

# 20
'''-----------------------------
a,b = input().split('-')
print(a,b,sep='')
-----------------------------'''

# 21
'''-----------------------------
a = input()
for i in range(len(a)):
    print(a[i])
-----------------------------'''
'''-----------------------------
a = input()
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
-----------------------------'''

# 22
'''-----------------------------
a = input()
print(a[:2],a[2:4],a[4:6])
-----------------------------'''

# 23
'''-----------------------------
a,b,c = input().split(':')
print(b)
-----------------------------'''

# 24
'''-----------------------------
a,b = input().split()
print(a,b,sep='')
-----------------------------'''
'''-----------------------------
a,b = input().split()
print(a+b)
-----------------------------'''

# 25
'''-----------------------------
a,b = input().split()
print(int(a)+int(b))
-----------------------------'''

# 26
'''-----------------------------
a = input()
b = input()
print(float(a)+float(b))
-----------------------------'''

# 27
'''-----------------------------
a = input()
n = int(a)
print('%x'%n)
-----------------------------'''

# 28
'''-----------------------------
a = input()
n = int(a)
print('%X'%n)
-----------------------------'''

# 29
'''-----------------------------
a = input()
n = int(a,16)
print('%o'%n)
-----------------------------'''

# 30
'''-----------------------------
a = input()
u = ord(a)
print(u)
-----------------------------'''

# 31
'''-----------------------------
a = input()
u = chr(int(a))
print(u)
-----------------------------'''

# 32
'''-----------------------------
a = input()
b = -int(a)
print(b)
-----------------------------'''

# 33
'''-----------------------------
a = input()
b = ord(a)
c = chr(b+1)
print(c)
-----------------------------'''

# 34
'''-----------------------------
a,b = input().split()
print(int(a)-int(b))
-----------------------------'''

# 35
'''-----------------------------
a,b = input().split()
print(float(a)*float(b))
-----------------------------'''

# 36
'''-----------------------------
a,b = input().split()
c = str(a) * int(b)
print(c)
-----------------------------'''

# 37
'''-----------------------------
a = input()
b = input()
c = int(a) * str(b)
print(c)
-----------------------------'''

# 38
'''-----------------------------
a,b = input().split()
c = pow(int(a),int(b))
print(c)
-----------------------------'''
'''-----------------------------
a,b = input().split()
c = int(a)**int(b)
print(c)
-----------------------------'''

# 39
'''-----------------------------
a,b = input().split()
c = float(a)**float(b)
print(c)
-----------------------------'''
'''-----------------------------
a,b = input().split()
c = pow(float(a),float(b))
print(c)
-----------------------------'''

# 40
'''-----------------------------
a,b = input().split()
c = int(a)//int(b)
print(c)
-----------------------------'''

# 41
'''-----------------------------
a,b = input().split()
c = int(a)%int(b)
print(c)
-----------------------------'''

# 42
'''-----------------------------
a = input()
b = round(float(a),2)
print(b)
-----------------------------'''
'''-----------------------------
a = input()
b = format(float(a),'.2f')
print(b)
-----------------------------'''

# 43
'''-----------------------------
a,b = input().split()
c = float(a)/float(b)
print(format(c,'.3f'))
-----------------------------'''

# 44
'''-----------------------------
a,b = input().split()
print(int(a)+int(b))
print(int(a)-int(b))
print(int(a)*int(b))
print(int(a)//int(b))
print(int(a)%int(b))
c = float(a)/float(b)
print(format(c,'.2f'))
-----------------------------'''

# 45
'''-----------------------------
a,b,c = input().split()
sum = int(a)+int(b)+int(c)
avg = float(sum/3)
print(sum,end=' ')
print(format(avg,'.2f'))
-----------------------------'''
'''-----------------------------
a,b,c = input().split()
sum = int(a)+int(b)+int(c)
avg = sum/3
print(sum,format(avg,'.2f'))
-----------------------------'''

# 46
'''-----------------------------
a = input()
n = 2*int(a)
print(n)
-----------------------------'''
'''-----------------------------
a = input()
n = int(a)<<1
print(n)
-----------------------------'''

# 47
'''-----------------------------
a,b = input().split()
n = int(a)*pow(2,int(b))
print(n)
-----------------------------'''
'''-----------------------------
a,b = input().split()
n = (int(a)<<int(b))
print(n)
-----------------------------'''

# 48
'''-----------------------------
a,b = input().split()
n = int(a) < int(b)
print(n)
-----------------------------'''

# 49
'''-----------------------------
a,b = input().split()
n = int(a) == int(b)
print(n)
-----------------------------'''

# 50
'''-----------------------------
a,b = input().split()
n = int(a) <= int(b)
print(n)
-----------------------------'''

# 51
'''-----------------------------
a,b = input().split()
n = int(a) != int(b)
print(n)
-----------------------------'''

# 52
'''-----------------------------
a = input()
x = int(a) != 0
print(x)
-----------------------------'''
'''-----------------------------
a = input()
x = bool(int(a))
print(x)
-----------------------------'''

# 53
'''-----------------------------
a = input()
n = bool(int(a)) == False
print(n)
-----------------------------'''
'''-----------------------------
a = input()
n = bool(int(a))
print(not n)
-----------------------------'''

# 54
'''-----------------------------
a,b = input().split()
n = bool(int(a)) and bool(int(b))
print(n)
-----------------------------'''

# 55
'''-----------------------------
a,b = input().split()
n = bool(int(a)) or bool(int(b))
print(n)
-----------------------------'''

# 56
'''-----------------------------
a,b = input().split()
a = int(a)
b = int(b)
n = (bool(a) and (not bool(b))) or ((not bool(a)) and bool(b))
print(n)
-----------------------------'''

# 57
'''-----------------------------
a,b = input().split()
a,b = int(a),int(b)
n = bool(a) == bool(b)
print(n)
-----------------------------'''

# 58
'''-----------------------------
a,b = input().split()
a,b = int(a),int(b)
n = (not bool(a)) and (not bool(b))
print(n)
-----------------------------'''

# 59
'''-----------------------------
a = input()
n = ~int(a)
print(n)
-----------------------------'''

# 60
'''-----------------------------
a,b = input().split()
n = int(a) & int(b)
print(n)
-----------------------------'''

# 61
'''-----------------------------
a,b = input().split()
n = int(a) | int(b)
print(n)
-----------------------------'''

# 62
'''-----------------------------
a,b = input().split()
n = int(a) ^ int(b)
print(n)
-----------------------------'''

# 63
'''-----------------------------
a,b = input().split()
a,b = int(a),int(b)
m = max(a,b)
print(m)
-----------------------------'''
'''-----------------------------
a,b = input().split()
a,b = int(a),int(b)
result = (a if (a>=b) else b)
print(result)
-----------------------------'''

# 64
'''-----------------------------
a,b,c = input().split()
a,b,c = int(a),int(b),int(c)
print(min(a,b,c))
-----------------------------'''
'''-----------------------------
a,b,c = input().split()
a,b,c = int(a),int(b),int(c)
result = ((a if (a<=b) else b) if ((a if (a<=b) else b) <=c) else c )
print(result)
-----------------------------'''

# 65
'''-----------------------------
a,b,c = input().split()
a,b,c = int(a),int(b),int(c)
if a%2 == 0:
    print(a)
if b%2 == 0:
    print(b)
if c%2 == 0:
    print(c)
-----------------------------'''

# 66
'''-----------------------------
a,b,c = input().split()
a,b,c = int(a),int(b),int(c)
if a%2 == 0:
    print('even')
else:
    print('odd')
if b%2 == 0:
    print('even')
else:
    print('odd')
if c%2 == 0:
    print('even')
else:
    print('odd')
-----------------------------'''

# 67
'''-----------------------------
a = input()
a = int(a)
if a<0:
    if a%2==0:
        print('A')
    else:
        print('B')
else:
    if a%2==0:
        print('C')
    else:
        print('D')

-----------------------------'''

# 68
'''-----------------------------
a = input()
a = int(a)
if a>=90:
    print('A')
elif a>=70:
    print('B')
elif a>=40:
    print('C')
else:
    print('D')
-----------------------------'''

# 69
'''-----------------------------
x = input()
if x == 'A':
    print('best!!!')
elif x == 'B':
    print('good!!')
elif x == 'C':
    print('run!')
elif x == 'D':
    print('slowly~')
else:
    print('what?')
-----------------------------'''

# 70
'''-----------------------------
ss = input()
ss = int(ss)
if ss == 12 or ss == 1 or ss == 2:
    print('winter')
elif 3<= ss <=5:
    print('spring')
elif 6<= ss <=8:
    print('summer')
elif 9<= ss <=11:
    print('fall')
-----------------------------'''

# 71
'''-----------------------------
while True:
    a = input()
    a = int(a)
    if a==0:
        break
    print(a)
-----------------------------'''
'''-----------------------------
a=1
while a!=0:
    a=int(input())
    if a!=0:
        print(a)
    else:
        break
-----------------------------'''

# 72
'''-----------------------------
a = int(input())
while a>0:
    print(a)
    a = a-1
-----------------------------'''

# 73
'''-----------------------------
a = int(input())
while a>0:
    a = a-1
    print(a)
-----------------------------'''

# 74
'''-----------------------------
x = input()
xx = ord(x)
y = 97
while xx>=y:
    print(chr(y),end=' ')
    y = y+1
-----------------------------'''

# 75
'''-----------------------------
n = int(input())
i = 0
while n>=i:
    print(i)
    i = i+1
-----------------------------'''

# 76
'''-----------------------------
n = int(input())
for i in range(n+1):
    print(i)
-----------------------------'''

# 77
'''-----------------------------
n = int(input())
sum = 0
for i in range(n+1):
    if i%2 == 0:
        sum = sum + i
print(sum)
-----------------------------'''

# 78
'''-----------------------------
a = input()
while a != 'q':
    print(a)
    a = input()
if a == 'q':
    print(a)
-----------------------------'''

# 79
'''-----------------------------
n = int(input())
sum = 0
i = 1
while True:
    sum = sum+i
    if sum>=n:
        break
    else:
        i = i+1
print(i)
-----------------------------'''

# 80
'''-----------------------------
n,m = input().split()
n,m = int(n),int(m)
for i in range(1,n+1):
    for j in range(1,m+1):
        print(i,j)
-----------------------------'''

# 81
'''-----------------------------
x = input()
for i in range(1,16):
    xx = int(x,16)*i
    print(x,'*','{:#X}'.format(i)[2:],'=','{:#X}'.format(xx)[2:],sep='')
-----------------------------'''
'''-----------------------------
x = input()
for i in range(1,16):
    xx = int(x,16)*i
    print(x,'*','%X'%i,'=','%X'%xx,sep='')
-----------------------------'''

# 82
'''-----------------------------
n = int(input())
for i in range(1,n+1):
    if i%10==3 or i%10==6 or i%10==9:
        print('X',end=' ')
    else:
        print(i,end=' ')
-----------------------------'''

# 83
'''-----------------------------
r,g,b = input().split()
r,g,b = int(r),int(g),int(b)
rgb = r*g*b
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i,j,k)
print(rgb)
-----------------------------'''

# 84
'''-----------------------------
h,b,c,s = input().split()
h,b,c,s = int(h),int(b),int(c),int(s)
result = h*b*c*s/8/pow(2,20)
print(round(result,1),'MB')
-----------------------------'''

# 85
'''-----------------------------
w,h,b = input().split()
w,h,b = int(w),int(h),int(b)
result = w*h*b/8/pow(2,20)
print('%.2f'%result,'MB')
-----------------------------'''

# 86
'''-----------------------------
n = int(input())
sum = 0
i = 1
while True:
    sum = sum+i
    i = i+1
    if sum>=n:
        break
print(sum)
-----------------------------'''
'''-----------------------------
n = int(input())
sum = 0
i = 1
while True:
    if sum < n:
        sum = sum+i
        i = i+1
    else:
        break
print(sum)
-----------------------------'''

# 87
'''-----------------------------
n = int(input())
for i in range(1,n+1):
    if i%3!=0:
        print(i,end=' ')
-----------------------------'''

# 88
'''-----------------------------
a,d,n = input().split()
a,d,n = int(a),int(d),int(n)
result = a + (d*(n-1))
print(result)
-----------------------------'''

# 89
'''-----------------------------
a,r,n = input().split()
a,r,n = int(a),int(r),int(n)
result = a * (pow(r,(n-1)))
print(result)
-----------------------------'''

# 90
'''-----------------------------
a,m,d,n = input().split()
a,m,d,n = int(a),int(m),int(d),int(n)
for i in range(1,n):
    a = (a * m) + d
print(a)
-----------------------------'''

# 91
'''-----------------------------
a,b,c=input().split()
a,b,c=int(a),int(b),int(c)
d=1
while d%a!=0 or d%b!=0 or d%c!=0:
    d=d+1
print(d)
-----------------------------'''

# 92
'''-----------------------------
n = int(input())
a = input().split()
b = []
for i in range(n):
    a[i] = int(a[i])
for i in range(24):
    b.append(0)
for i in range(n):
    b[a[i]] += 1
for i in range(1,24):
    print(b[i],end=' ')
-----------------------------'''

# 93
'''-----------------------------
n = int(input())
a = input().split()
for i in range(1,n+1):
    print(a[-i],end=' ')
-----------------------------'''
'''-----------------------------
n = int(input())
a = input().split()
for i in range(n-1,-1,-1):
    print(a[i],end=' ')
-----------------------------'''

# 94
'''-----------------------------
n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
print(min(a))
-----------------------------'''
'''----------------------------
n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
b = sorted(a)
print(b[0])
-----------------------------'''

# 95
'''-----------------------------
d = []
for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)
n = int(input())
for i in range(n):
    x,y = input().split()
    d[int(x)][int(y)] = 1
for i in range(1,20):
    for j in range(1,20):
        print(d[i][j],end=' ')
    print()
-----------------------------'''
'''-----------------------------
d = []
d = [[0 for j in range(20)]for i in range(20)]
n = int(input())
for i in range(n):
    x,y = input().split()
    d[int(x)][int(y)] = 1
for i in range(1,20):
    for j in range(1,20):
        print(d[i][j],end=' ')
    print()
-----------------------------'''

# 96
'''-----------------------------
c=[]
d=[]
for i in range(20):
    c.append([])
    for j in range(20):
        c[i].append(0)

for i in range(19):
    c = list(map(int,input().split()))
    d.append(c)

n = int(input())
for i in range(n):
    x,y=input().split()
    for j in range(19):
        if d[int(x)-1][j] == 0:
            d[int(x)-1][j] = 1
        else:
            d[int(x)-1][j] = 0

        if d[j][int(y)-1] == 0:
            d[j][int(y)-1] = 1
        else:
            d[j][int(y)-1] = 0

for i in range(19):
    for j in range(19):
        print(d[int(i)][int(j)],end=' ')
    print()
-----------------------------'''

# 97
'''-----------------------------
w,h = map(int,input().split())
a = []
for i in range(w):
    a.append([])
    for j in range(h):
        a[i].append(0)

n = int(input())
for i in range(n):
    l,d,x,y = map(int,input().split())
    for j in range(l):
        if d == 0:
            a[x-1][(y-1)+int(j)] = 1
        else:
            a[(x-1)+int(j)][y-1] = 1

for i in range(w):
    for j in range(h):
        print(a[int(i)][int(j)],end=' ')
    print()
-----------------------------'''

# 98
'''-----------------------------
a = []
d = []
for i in range(10):
    a.append([])
    for j in range(10):
        a[i].append(0)

for i in range(10):
    a = list(map(int,input().split()))
    d.append(a)

i,j =int(1),int(1)
while i<10 and j<10:
    if d[i][j] == 0:
        d[i][j] = 9
        j = j+1
    elif d[i][j] == 1:
        i = i+1
        j = j-1
    elif d[i][j] == 2:
        d[i][j] = 9
        break

for i in range(10):
    for j in range(10):
        print(d[i][j],end=' ')
    print()
-----------------------------'''