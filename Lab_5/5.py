import re
inp = input()
reg = re.findall("a.*b", inp)

print(reg)