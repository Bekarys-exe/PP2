import datetime

a = datetime.datetime.now()
b = a - datetime.timedelta(days=5)

print("Date 5 days ago:" , b)
print("Date Now:" , a)
