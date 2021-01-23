#!/usr/bin/env python3
# coding=utf-8

# L = []
# n = 1
# while n <= 99:
#     L.append(n)
#     n = n + 2

# half_len = int(len(L) / 2)

# m = 0
# while m < half_len:
#     print(L[m])
#     m = m + 1


#     [0,3]
#     (0,3] #我是冲突

# d = {'a' : 1, 'b' : 2, 'c' : 3}
# for key in d:
#     print(key)

# from collections import Iterable
# isinstance('abc', Iterable)

# for i, value in enumerate(['A', 'B', "c"]):
#     print(i, value)

# for x, y in [(1,2), (2,3), (3,4), (4,5)]:
#     print(x,y)

# def find_min_max(L):
#     if len(L)==0:
#         return (None, None)
#     else:
#         maxL=L[0]
#         minL=L[0]
#         for i in L:
#             if maxL < i:
#                 maxL = i
#             if minL > i:
#                 minL = i
#         return(maxL, minL)

# print(find_min_max([0,4,6,3,2,8])) #我是冲突



# L = []
# for i in range(1, 10):
#     K = []
#     for j in range(i):
#         print(L)
#         if j == 1 or j == i:
#             L[i][j] = 1
#         else:
#             L[i][j] = L[i-1][j-1] + L[i-1][j]

# def add(x, y, f):
#     return f(x) + f(y)
# print(add(-5, 6, abs))

# def f(x):
#     return x * x
# r=map(str, [1, 2, 3, 4, 5])
# print(list(r))

# from functools import reduce
# def add(x, y):
#     return x + y

# print(reduce(add, [1, 3, 4, 5, 7, 9]))

# from functools import reduce
# def fn(x, y):
#     return x * 10 + y
# print(reduce(fn, [1, 3, 5, 7, 9]))

# def normalize(name):
#     return name.capitalize()
# l=list(map(normalize, ['adam', 'LIZA', 'barT']))
# print(l)

# from functools import reduce
# def str2float(s):
#     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,'8': 8, '9': 9}
#     s1, s2 = s.split('.') 
#     def fn(x, y):
#         return x * 10 + y
#     def char2num(s):
#         return digits[s]
#     f1 = reduce(fn, map(char2num, s1))
#     f2 = reduce(fn, map(char2num, s2))/(10**len(s2))
#     return f1 + f2

# print(str2float('123.456'))

    
# def not_empty(s):
#     res = s and s.strip()
#     print(res)
#     return res


# print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  D  D'])))

# def is_palindrome(n):
#     arr = str(n)
#     flag = True
#     a, b = 0, len(arr)-1
#     if b <= 1:
#         if arr[a] != arr[b]:
#             flag = False

#     while not(a == b or a == b - 1):
#         print(a, b)
#         if arr[a] != arr[b]:
#             flag = False
#         a = a + 1
#         b = b - 1
#     return flag

# print(is_palindrome(7))

# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#             return i * i
#         fs.append(f)
#     return fs

# f1, f2, f3 = count()

classmates = [{"name": "wxs", "age": 18}, {"name": "lml", "age": 32}, {"name": "lml2", "age": 33}, {"name": "2lml", "age": 19}]
def filter_foo(item):
    return item["age"] < 30
result = filter(filter_foo, classmates)
print(list(result))
#这是一个注释
'''
这是多行注释
打印
hello
‘’‘
print('hello, world!')

# 主食123
