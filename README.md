# Antivirus
A simple antivirus software
This is meant to be a proof of concept with the end goal being a functioning application capable of detecting
basic known malware

Roadmap:
-  [x] Scan the current directory for known sha256, sha1, and md5 hashes
-  [ ] Split up program using multiple files and subprocesses
-  [x] Command line args
-  [x] Scanning network ports to check for malicious port connects
-  [ ] IP scanning
-  [ ] Optimize scanning process using multithreading or cached data
-  [ ] API calls from MalwareBazaar for updated malware list once a day
-  [ ] Implementing ML learning to predict probability of a file being a virus or malicious port connection
-  [ ] GUI and responsive design using Django or Flask w/ React



Credits:
* Len Stevens for inspiration: https://github.com/Len-Stevens