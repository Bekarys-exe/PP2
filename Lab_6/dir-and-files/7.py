import shutil

source_file = input("Enter the source filename: ")  
destination_file = input("Enter the destination filename: ")  

try:
    shutil.copyfile(source_file, destination_file)  
    print(f"File '{source_file}' has been copied to '{destination_file}'.")
except FileNotFoundError:
    print("Error: The source file does not exist.")
except Exception as e:
    print("An error occurred:", e)
