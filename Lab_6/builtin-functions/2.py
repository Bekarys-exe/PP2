str = input("Write your str please: ")

upper_count = sum(1 for x in str if x.isupper())
lower_count = sum(1 for x in str if x.islower())

print(upper_count)
print(lower_count)