# OS Library

import os

def os_demo():

    print("1. Current Working Directory")
    cwd = os.getcwd()
    print("CWD:", cwd)

    print("\n2. Create Directory")
    if not os.path.exists("os_demo"):
        os.mkdir("os_demo")
        print("Directory created: os_demo")

    sub_dir = os.path.join("os_demo", "data")
    if not os.path.exists(sub_dir):
        os.mkdir(sub_dir)
        print("Subdirectory created:", sub_dir)

    file_path = os.path.join(sub_dir, "example.txt")
    with open(file_path, "w") as f:
        f.write("Heyyy! I am Krisha..")
    print("File created:", file_path)

    print("\n5. List Files in data folder")
    print(os.listdir(sub_dir))

    print("\n6. Path Information")
    print("Exists:", os.path.exists(file_path))
    print("Is File:", os.path.isfile(file_path))
    print("Is Directory:", os.path.isdir(sub_dir))
    print("Absolute Path:", os.path.abspath(file_path))

    new_file_path = os.path.join(sub_dir, "renamed_example.txt")
    os.rename(file_path, new_file_path)
    print("File renamed")

if __name__ == "__main__":
    os_demo()
