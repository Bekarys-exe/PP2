import datetime

a = datetime.datetime.now()

b = a - datetime.timedelta(days=1)

x = (a-b).total_seconds()

print(x)