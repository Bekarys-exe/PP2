def squares_generator(N):
    for i in range(N):
        yield i ** 2

N = int(input("Write your number please: "))

for squares in squares_generator(N):
    print(squares)