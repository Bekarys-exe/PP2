import datetime

a = datetime.datetime.now()

b = a.strftime("%x "+ "%X" )

print(b)

"""Можно написать и по другому:

import datetime

a = datetime.datetime.now()

b = a.replace(microsend = 0)

print(b)


"""