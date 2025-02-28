import re
inp = input()
reg = re.findall("[A-Z][^A-Z]*", inp)

print(reg)