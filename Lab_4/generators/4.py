def square_of_numbers_from_a_to_b(A , B):
    for i in range( A , B+1):
        yield i**2

A = int(input("Write your Star number please: "))
B = int(input("Write your Final number please: "))

print(*square_of_numbers_from_a_to_b(A , B) , sep= ", ")

"""
Можно написать и вот так 

for squares in square_of_numbers_from_a_to_b(A , B):
    print(squares)
"""