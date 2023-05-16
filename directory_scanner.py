import os
import hashlib
import sys

def sha256_file(filename):
    with open(filename, 'rb') as f:
        file_content = f.read()
    hash_value = hashlib.sha256(file_content)
    return hash_value.hexdigest()

def sha1_file(filename):
    with open(filename, 'rb') as f:
        file_content = f.read()
    hash_value = hashlib.sha1(file_content)
    return hash_value.hexdigest()

def md5_file(filename):
    with open(filename, 'rb') as f:
        file_content = f.read()
    hash_value = hashlib.md5(file_content)
    return hash_value.hexdigest()

def scan_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            filename = os.path.join(root, file)
            print(f"Filename: {filename}, Sha256: {sha256_file(filename)}, Sha1: {sha1_file(filename)}, Md5 {md5_file(filename)}")

def main():
    directory = os.getcwd()
    scan_directory(directory)
    
if __name__ == '__main__':
    main()