import re
inp = input()
reg = re.findall("[A-Z][^A-Z]*", re.sub(" ", "", inp))

ans = reg[0]
for i in reg[1:]:
    ans += " " + i

print(ans)