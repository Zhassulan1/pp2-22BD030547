import os

path = input("Enter path:\n")
if not os.access(path, os.F_OK):
    print("Wrong path")
    exit()

info_tuple = input("Path found!\nEnter the list:\n")
info_str = ""

for i in info_tuple:
    info_str += i

with open(path, 'w') as file:
    file.write(info_str)