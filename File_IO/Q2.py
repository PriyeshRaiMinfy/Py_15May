import os

def create_file(filename, content="THIS IS THE DEFAULT CONTENT OF A FILE"): # ye default content hai
    with open(filename, 'w') as file:
        file.write(content)
    print(f"File '{filename}'  : content is addedd to the given file....")
#--------------------------------------------------------------------------------------------------
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())
    
    except FileNotFoundError:      # <-------------- 
        ("Error : File doesnt exist...!")
#--------------------------------------------------------------------------------------------------
def delte_file(filename):
    try:
        os.remove(filename)
    except FileNotFoundError:
        ("Error : No File to Delete")
#--------------------------------------------------------------------------------------------------
def lst_dir():
    try:
        files = os.listdir()
        if not files:
            print("Derectory is Empty")
        else:
            for items in files:
                print(items)
    except FileNotFoundError:
        print("Error : No Such Directory Found")

#--------------------------------------------------------------------------------------------------
def cng_dir(path):
    try:
        os.chdir(path)
    except FileExistsError:
        os.mkdir(path)
        os.chdir(path)
        print(f"Directory ceated : '{path}'")
    print(f"Current directory => {os.getcwd()}")





#--------------------------------------------------------------------------------------------------
def operation():
    uinput = input("Enter the command : ")
    commandline = list(uinput.split('"'))
    # print(commandline)
    cmd = [x.strip() for x in commandline if x.strip()]
    # print(cmd)
    # print(len(commandline))
    # print(len(cmd))
    # print(type(cmd[0]))
    # print(cmd[1])
    # print(cmd[2])

    command_map = {
        "touch": create_file,
        "read": read_file,
        "delete": delte_file,
        "ls":lst_dir,
        "cd":cng_dir
    }


    command_map[cmd[0]](*cmd[1:])

# ------------------ Main() function-----------------------
operation()
