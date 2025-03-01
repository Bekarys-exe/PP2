filename = input("Enter the filename: ") 

try:
    with open(filename, 'r', encoding='utf-8') as file:
        line_count = sum(1 for line in file)  
    print(f"Number of lines in '{filename}': {line_count}")
except FileNotFoundError:
    print("File not found. Please check the filename and try again.")
