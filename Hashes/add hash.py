import os

def check_and_add_input(file_path):
    user_input = input("Enter a value: ")

    if not os.path.isfile(file_path):
        with open(file_path, 'w') as file:
            file.write(user_input + '\n')
        print("Input added to the file.")
    else:
        with open(file_path, 'r+') as file:
            if user_input in file.read():
                print("Input already exists in the file.")
            else:
                file.write('\n' + user_input)
                print("Input added to the file.")

file_path = "full_sha256.txt"
while True:
    check_and_add_input(file_path)
