'''5 . Write a program to check if the given number is a palindrome number.'''

n = int(input("enter a three digit number"))
term = n
rev = 0
while n > 0 :
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10 
    print(rev)
if term == rev:
    print("the number is palindrome ")
else:
    print("the number is not a palindrome")    