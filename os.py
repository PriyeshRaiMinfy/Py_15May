import os

def list_dir(path, indent=0):
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        print('  ' * indent + entry)
        # if os.path.isdir(full_path):
        #     list_dir(full_path, indent + 1)

list_dir('.') 
