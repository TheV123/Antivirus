import socket
import subprocess
import sys
from datetime import datetime
import antivirus

def scan_ports():
    # subprocess.call('clear', shell=True)
    
    START_PORT = 1
    END_PORT = 65535    
    # print("hello")
    for port in range(START_PORT, END_PORT):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.01)
            result = sock.connect_ex(('localhost', port))
            if result == 0:
                service = socket.getservbyport(port)
                if port in antivirus.malious_ports:
                    print(f'Your computer appears to be connected to malicious port {port}')
                else:
                    print(f"Your computer is connected to port {port} with service {service}")
            sock.close()
        except KeyboardInterrupt:
            print("Exiting...")
            sys.exit()
        except socket.error:
            print(f"Service on {port} is unknown")
