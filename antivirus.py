import hashlib
import os
import directory_scanner
import port_scanner
import args

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
    
    
if __name__ == '__main__':
    store_hashes()
    arguments = args.parse_args()
    if arguments.directory:
        directory_scanner.scan_directory(arguments)
    if arguments.scan_ports:
        port_scanner.scan_ports()