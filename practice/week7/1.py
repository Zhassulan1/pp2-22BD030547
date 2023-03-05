import os

def file_edit(fname, ed_mode, information):
    with open(fname, mode = ed_mode) as file:
        file.write(information)


def exist(fname):
        return os.path.exists(fname)
    
def createFile(fname):
    if exist(fname):
        return
    file = open(fname, 'w')
    file.close()




def readFile(fname):
    if not exist(fname):
        print(f"file {fname} does not exist, choose '1' to create file")
        return

    file = open(fname, 'r')
    try:
        readf = file.read()
        print(readf)
    finally:
    
        file.close()

def appendFile(fname, text):
    if not exist(fname):
        print(f'file {fname} does not exist')
        return
    
    file_edit(fname, 'a', text)

def overwriteFile(fname,text):
    if not exist(fname):
        print(f"file {fname} does not exist")
        return
    
    file_edit(fname, 'w', text)
    

def removeFile(fname):
    if not exist(fname):
        print(f" file {fname} does not exist")
        return

    os.remove(fname)
    print(f"file {fname} was removed")


print('Welcome to my blog!\nWhat do you want to do with files/the file?')
option = int(input('Options(type a number):\n1-Create a new file\n2-Read existing file\n3-Update some information in a file\n4-Overwrite all content in a file\n5-Remove existing file\nWrite a number(1-5): '))

file_name = input('Please enter a file name (no extension, .txt will be added automatically):').strip()
file_name = os.path.join( 
    os.getcwd(), "practice", "week7",  file_name + ".txt"
    )

if option == 1:
    if file_name:
        createFile(file_name)
    else:
        print("Enter proper name")
elif option == 2:
    readFile(file_name)
elif option == 3:
    appendFile(file_name)
elif option == 4:
    overwriteFile(file_name)
elif option == 5:
    removeFile(file_name)
else:
    print('Something went wrong!')