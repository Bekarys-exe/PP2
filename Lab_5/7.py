import re
inp = input()
reg = re.split("_", inp)

ans = reg[0]
for i in reg[1:]:
    ans += i[0].upper() + i[1:]

print(ans)