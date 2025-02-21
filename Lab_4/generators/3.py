def special_generator(N):
    for i in range(N):
        if i == 0:
            continue
        if (i % 12 != 0):
            continue
        yield i

N = int(input("Write your number sir: "))
print(*special_generator(N) , sep= ", ")        