import os

path1 = input("Enter the path to copy from:\n")
path2 = input("Enter the path where to copy:\n")

copy = ""
with open(path1, 'r') as file1:
    copy = file1.read()

print(copy)
with open(path2, 'w') as file2:
    file2.write(copy)