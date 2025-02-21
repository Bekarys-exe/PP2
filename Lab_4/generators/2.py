def even_numbers_generator(N):
    for i in range(N):
        if(i % 2 != 0):
            continue
        yield i  

N = int(input("Input your sum please: "))

print(*even_numbers_generator(N) , sep= ", ")