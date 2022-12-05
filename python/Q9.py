'''9 . Write a program to accept a number from a user and calculate the sum of all numbers from 1 to that given number'''

a =int(input('enter a number'))

i = 0
for x in range(1,a + 1,):
    i = i + x
    print(i)
    