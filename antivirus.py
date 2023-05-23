import hashlib
import os
import directory_scanner
import port_scanner
import args
import csv

md5_malware_hashes = []
sha1_malware_hashes = []
sha256_malware_hashes = []
malious_ports = []

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
    
    global malious_ports
    #gotten from https://docs.trendmicro.com/all/ent/officescan/v10.5/en-us/osce_10.5_olhcl/osce_topics/what_are_trojan_ports_.htm
    with open('malicious_ports.csv', 'r') as f:
        csv_file = csv.DictReader(f, delimiter = ',')
        for line in csv_file:
            malious_ports.append(line['Port Number'])
    
    print(malious_ports)
if __name__ == '__main__':
    store_hashes()
    arguments = args.parse_args()
    if arguments.directory:
        directory_scanner.scan_directory(arguments)
    if arguments.scan_ports:
        port_scanner.scan_ports()