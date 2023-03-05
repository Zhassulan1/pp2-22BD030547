import os

def get_dirs(list):
    dirs = []
    for l in list:
        if os.path.isdir(l):
            dirs.append(l)
    return dirs


def get_files(list):
    files = []
    for l in list:
        if os.path.isfile(l):
            files.append(l)
    return files


path = os.getcwd()

mode = input(
    "1 - only dirs\n2 - files and dirs\n3 - only files\n"
)

if mode == "1":
    print(get_dirs(os.listdir(path)))
elif mode == "2":
    print(os.listdir(path))
elif mode == "3":
    print(get_files(os.listdir(path)))
else:
    print("incorrect input")