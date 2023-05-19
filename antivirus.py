import os
import sys
import args
import directory_scanner


md5_malware_hashes = []
sha1_malware_hashes = []
sha256_malware_hashes = []


def store_hashes():
    global md5_malware_hashes
    #gotten from https://github.com/Len-Stevens/MD5-Malware-Hashes/tree/main
    with open("MD5_hashes.txt", "r") as f:
        md5_malware_hashes = f.read().splitlines()
    
    #gotten from MalwareBazaar https://bazaar.abuse.ch/export/
    global sha1_malware_hashes
    with open("full_sha1.txt", "r") as f:
        sha1_malware_hashes = f.read().splitlines()[9:-1]
    
    global sha256_malware_hashes
    #gotten from MalwareBazaar https://bazaar.abuse.ch/export/
    with open("full_sha256.txt", "r") as f:
        sha256_malware_hashes = f.read().splitlines()[9:-1]
        

def arguments_parser():
    arguments = args.parse_args()
    #check the arguments if -s flag is there
    directory_scanner.scan_directory(args)
    

if __name__ == 'main':
    store_hashes()
    arguments_parser()