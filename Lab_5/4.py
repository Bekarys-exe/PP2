import re
inp = input()
reg = re.findall("[A-Z][a-z]+", inp)

print(reg)