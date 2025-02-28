import re
inp = input()
reg = re.findall("[A-Z][^A-Z]*", inp)

ans = re.sub("[A-Z][^A-Z]*", "", inp)
for i in reg:
    ans += "_" + i[0].lower() + i[1:]

print(ans)