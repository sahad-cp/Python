b = 10
try:
    a = 9/b
    print(a)
    print('try completed')
except ZeroDivisionError:
    print("Can't divided by zero")