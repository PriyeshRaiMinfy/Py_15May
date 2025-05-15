import os

def create_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    print(f"File '{filename}'  : content is addedd to the given file....")

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())
    
    except FileNotFoundError:
        ("Error : File doesnt exist...!")
def delte_file(filename):
    try:
        os.remove(filename)
    except FileNotFoundError:
        ("Error : No File to Delete")


# -----------------------
create_file('example4.txt', "Hello, My name is Priyesh.\n I am a tech intern at minfy")
print("----------------------------------------------------------")
read_file('example4.txt')
