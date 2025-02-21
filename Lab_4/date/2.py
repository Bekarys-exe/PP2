import datetime
#можно убрать Only_date если нужно со временем и прочей хуйней
a = datetime.datetime.now()
Only_date = a.date()
b = Only_date - datetime.timedelta(days=1)
c = Only_date + datetime.timedelta(days=1)

print("Yesterday:" , b)
print("Today:" , Only_date)
print("Tomorrow:" , c)