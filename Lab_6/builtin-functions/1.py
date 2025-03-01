from functools import reduce

Mylist = list(map(int , input("Write your numbers: ").split()))
result = reduce(lambda x , y: x*y , Mylist) 

print(result)