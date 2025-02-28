import re
inp = input()
reg = re.findall("[a-z]_[a-z]", inp)

print(reg)