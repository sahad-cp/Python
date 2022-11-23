import datetime

now = datetime.datetime.now()
print(now.strftime("%d/%m/%Y"))

x=datetime.datetime(2020,4,8)

dif = now-x
print(dif)