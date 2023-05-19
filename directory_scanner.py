import os
import hashlib
import sys
import args
import antivirus

def sha1_file(filename):
    with open(filename, 'rb') as f:
        file_content = f.read()
    hash_value = hashlib.sha1(file_content)
    return hash_value.hexdigest()

def sha256_file(filename):
    with open(filename, 'rb') as f:
        file_content = f.read()
    hash_value = hashlib.sha256(file_content)
    return hash_value.hexdigest()

def md5_file(filename):
    with open(filename, 'rb') as f:
        file_content = f.read()
    hash_value = hashlib.md5(file_content)
    return hash_value.hexdigest()

def sha1_scan(filename):
    with open(filename, 'r') as f:
        global sha1_malware_hashes
        if sha1_file(filename) in antivirus.sha1_malware_hashes:
            print("SHA1 hash matches a known malware hash!")

def sha256_scan(filename):
    with open(filename, 'r') as f:
        global md5_malware_hashes
        if sha256_file(filename) in antivirus.sha256_malware_hashes:
            print("SHA256 hash matches a known malware hash!")


def md5_scan(filename):
    with open(filename, 'r') as f:
        global md5_malware_hashes
        if md5_file(filename) in antivirus.md5_malware_hashes:
            print("MD5 hash matches a known malware hash!")


def scan_directory(args):
    directory = args.scan_directory
    # print(directory)
    for root, dirs, files in os.walk(directory):
        for file in files:
            filename = os.path.join(root, file)
            print(filename)
            md5_scan(filename)
            sha256_scan(filename)
            sha1_scan(filename)
