my_list = list(input("Write your list values please: ").split())

with open('row.txt', 'w', encoding='utf-8') as file:
    for item in my_list:
        file.write(item)
