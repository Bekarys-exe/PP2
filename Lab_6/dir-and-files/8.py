import os

file_path = input("Enter the file path to delete: ")

if os.path.exists(file_path):
    if os.access(file_path, os.W_OK):
        try:
            os.remove(file_path) 
            print(f"File '{file_path}' has been deleted successfully.")
        except Exception as e:
            print("An error occurred:", e)
    else:
        print("Error: No permission to delete the file.")
else:
    print("Error: The specified file does not exist.")
