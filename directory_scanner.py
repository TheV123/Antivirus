import os
import hashlib
import sys

md5_malware_hashes = []
sha256_malware_hashes = []

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

def sha256_scan(filename):
    with open(filename, 'r') as f:
        global md5_malware_hashes
        if sha256_file(filename) in sha256_malware_hashes:
            print("SHA256 hash matches a known malware hash!")


def md5_scan(filename):
    with open(filename, 'r') as f:
        global md5_malware_hashes
        if md5_file(filename) in md5_malware_hashes:
            print("MD5 hash matches a known malware hash!")


def scan_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            filename = os.path.join(root, file)
            md5_scan(filename)
            sha256_scan(filename)

def main():
    global md5_malware_hashes
    #gotten from https://github.com/Len-Stevens/MD5-Malware-Hashes/tree/main
    with open("MD5_hashes.txt", "r") as f:
        md5_malware_hashes = f.read().splitlines()
            
    global sha256_malware_hashes
    #gotten from MalwareBazaar https://bazaar.abuse.ch/export/#csv
    with open("full_sha256.txt", "r") as f:
        sha256_malware_hashes = f.read().splitlines()[9:-1]
    
    directory = os.getcwd()
    scan_directory(directory)
    
if __name__ == '__main__':
    main()