import re
inp = input()
reg = re.sub("[, .]", ":", inp)

print(reg)