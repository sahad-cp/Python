'''13 . Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690'''
n = int(input("enter a number"))

s = 0

a = 2
for i in range(n):

    s = s + a
    a = a * 10 + 2
    print(s) 
