from pathlib import Path

path = Path(input("Enter the directory path: "))  

directories = [d.name for d in path.iterdir() if d.is_dir()]
print("Directories:", directories)

files = [f.name for f in path.iterdir() if f.is_file()]
print("Files:", files)

all_items = [item.name for item in path.iterdir()]
print("All directories and files:", all_items)
