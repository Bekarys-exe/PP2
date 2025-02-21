def reverse(N):
    for i in range(N+1):
        yield N - i
       

N = int(input("Write your number: "))

print(*reverse(N) , sep= ", ")
