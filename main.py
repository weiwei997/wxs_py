#!/usr/bin/env python3
# coding=utf-8

# sum=0
# for x in range(101):
#     sum=sum+x
# print(sum)
# print(list(range(5)))
# print(range(101))
# lml = range(100)
# newlist = []
# for x in lml:
#     is_odd = (x % 2 == 1)
#     if is_odd:
#         newlist.append(x)
# print(newlist)
# sum = 0
# n = 99
# while n > 0:
#     sum = sum + n
#     n = n - 2
# print(sum)
# n=0
# while n < 100:
#     n = n + 1
#     print(n)
# n = 10
# while n <= 100:
#     n = n + 1
#     if n < 11:
#         break
#     print(n)
# a=abs(-100.20)
# print(a)
# a=max(1,2,3,4,100)
# print(a)

# x=abs(100)
# y=abs(-30)
# print(x,y)

# def my_abs(x):
#     if not isinstance(x,(int,float)):
#         raise TypeError('bad operand type')
#     if x >= 0:
#         return x
#     else:
#         return -x

# print(my_abs('a'))
# import math

# def move(x,y,step,angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx,ny

# x,y = move(10, 30, 100, math.pi/3)
# print(x,y)
# def power(x):
#     return x * x
# print(power(4))
# def power3(x, n):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s

# x4=power3(2, 4)
# print(x4)
# def power(x, n=2):
#     s=1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s

# print(power(5))

# def enroll(name, gender, age=6, city='beijing'):
#     print('name :', name)
#     print('gender :', gender)
#     print('age :', age)
#     print('city :', city)
# print (enroll('wxs', 'A', city='tianjin'))

# def add_end(l=None):
#     if l is None:
#         l = []
#     l.append('end')
#     return l
   
# print(add_end())

# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum

# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# print(calc(*nums))

# def person(name, age, **kw):
#     print('name:', name,'age:', age, 'others:', kw)

# extra = {'city':'beijing','job': 'hrbp'}
# xinxi=person('wxs', 26, **extra)
# print(xinxi)

# def product(*numbers):
#     if product is None:
#         pow = 0
#     else:
#         pow = 1
#         for n in numbers:              
#             pow = pow * n
#     return pow

# print(product())
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)


move(1, 'A', 'C', 'B')




def person(name, age, *, city, job):
    print(name, age, city, job)

person(1, 2, job=4, city=3)

def product(*numbers):
    pow = 1
    for n in numbers:
        pow = pow * n
    return pow


try:
    product()
    print('测试失败!')
except TypeError:
    print('测试成功!')
