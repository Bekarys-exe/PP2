import re

inp = input()
reg = re.fullmatch(("ab*"), inp)

if reg:
    print("The string contains 'a' followed by zero or more 'b''s.")
else:
    print("The string does not contain 'a' followed by zero or more 'b''s.")