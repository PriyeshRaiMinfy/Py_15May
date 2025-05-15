import os

def create_file(filename, content="THIS IS THE DEFAULT CONTENT OF A FILE"):
    with open(filename, 'w') as file:
        file.write(content)
    print(f"File '{filename}' : content is added to the given file....")

#--------------------------------------------------------------------------------------------------
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Error : File doesn't exist...!")

#--------------------------------------------------------------------------------------------------
def delete_file(filename):
    try:
        os.remove(filename)
        print(f"File '{filename}' deleted successfully.")
    except FileNotFoundError:
        print("Error : No file to delete.")

#--------------------------------------------------------------------------------------------------
def lst_dir():
    try:
        files = os.listdir()
        if not files:
            print("Directory is empty.")
        else:
            for items in files:
                print(items)
    except FileNotFoundError:
        print("Error : No such directory found.")

#--------------------------------------------------------------------------------------------------
def cng_dir(path):
    try:
        os.chdir(path)
    except FileNotFoundError:
        os.mkdir(path)
        os.chdir(path)
        print(f"Directory created: '{path}'")
    print(f"Current directory => {os.getcwd()}")

#--------------------------------------------------------------------------------------------------
def operation():
    command_map = {
        "touch": create_file,
        "read": read_file,
        "delete": delete_file,
        "ls": lst_dir,
        "cd": cng_dir
    }

    while True:
        uinput = input("Enter the command (or type 'exit' to quit): ").strip()
        if uinput.lower() == "exit":
            print("Exiting the program.")
            break

        commandline = list(uinput.split('"'))
        cmd = [x.strip() for x in commandline if x.strip()]

        if not cmd:
            print("No command entered.")
            continue

        if cmd[0] not in command_map:
            print("Invalid command.")
            continue

        try:
            command_map[cmd[0]](*cmd[1:])
        except TypeError as e:
            print(f"Error: {e}")

# ------------------ Main() function-----------------------
operation()
