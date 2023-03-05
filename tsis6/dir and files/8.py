import os

path = input("Enter the path to be deleted:\n")

if not os.access(path, os.F_OK):
    print("Wrong path")
    exit()
if not os.access(path, os.X_OK):
    print("Path is not available")
    exit()

os.remove(path)
print(f"File '{path}' was deleted successfully") 