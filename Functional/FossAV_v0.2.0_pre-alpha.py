import hashlib, os, multiprocessing

def process_file(file_path):
    try:
        # Process the file here
        # Example: Print the file path
        getSha256(file_path)
        checkHash(_hash)
        
    except Exception as e:
        print("An error occurred while processing the file:", file_path)
        print("Error:", str(e))

def count_files(directory):
    file_count = 0

    for entry in os.scandir(directory):
        try:
            if entry.is_file():
                file_count += 1
            elif entry.is_dir():
                file_count += count_files(entry.path)
        except PermissionError as e:
            print("Access denied:", entry.path)
        except Exception as e:
            print("An error occurred while scanning directory:", entry.path)
            print("Error:", str(e))

    return file_count

def traverse_directory(directory):
    total_files = count_files(directory)
    processed_files = 0
    progress_width = 50

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r') as f:
                    # Accessing the file in read mode to check if it throws an exception
                    pass
                process_file(file_path)
            except IOError as e:
                if e.errno == 13:  # Permission denied error code
                    # Handle access denied error
                    print("Access denied:", file_path)
                else:
                    # Handle other IO errors
                    print("IO Error:", str(e))
            except Exception as e:
                print("An error occurred while processing the file:", file_path)
                print("Error:", str(e))

            processed_files += 1
            print(processed_files)

            


def readToList(_from):
    file_path = _from

    global hashList
    
    hashList = []

    with open(file_path, 'r') as file:
        for line in file:
            hashList.append(line.strip())

def findLoc(target):
    global result
    script_path = os.path.abspath(__file__)
    target_folder = target
    current_folder = os.path.dirname(script_path)
    while current_folder != "/" and os.path.basename(current_folder) != target_folder:
        current_folder = os.path.dirname(current_folder)
    result = current_folder if os.path.basename(current_folder) == target_folder else "Target folder not found."



def getSha256(file):
    # Python program to find SHA256 hash string of a file
    global _hash
    filename = file
    sha256_hash = hashlib.sha256()
    with open(filename,"rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
        _hash = str(sha256_hash.hexdigest())

def getMd5(file):
    # Python program to find SHA256 hash string of a file
    global _hash
    filename = file
    md5_hash = hashlib.md5()
    with open(filename,"rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096),b""):
            md5_hash.update(byte_block)
        _hash = str(md5_hash.hexdigest())

def checkHash(myHash):
    global virusFound
    def check_string_in_file(file_path, search_string):
        with open(file_path, 'r') as file:
            file_contents = file.read()
            if search_string in file_contents:
                virusFound = 1

    # Usage
    file_path = result
    search_string = myHash

    if check_string_in_file(file_path, search_string):
        print("Virus Found")


findLoc('FossAV')
result = result + '\\Hashes (Md5, Sha256, etc)\\full_sha256.txt'

current_user = os.getlogin()
# Set the directory to start traversing from
start_directory = 'C:/Users/' + current_user

virusFound = 0

# Traverse the directory recursively
traverse_directory(start_directory)
print('done')

print(virusFound)
