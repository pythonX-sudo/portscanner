import socket
import IPy

print('''
______          _     _____                                 
| ___ \        | |   /  ___|                                
| |_/ /__  _ __| |_  \ `--.  ___ __ _ _ __  _ __   ___ _ __ 
|  __/ _ \| '__| __|  `--. \/ __/ _` | '_ \| '_ \ / _ \ '__|
| | | (_) | |  | |_  /\__/ / (_| (_| | | | | | | |  __/ |   
\_|  \___/|_|   \__| \____/ \___\__,_|_| |_|_| |_|\___|_|                                                                                                                           

Created by PythonX ~ ShahadathAkash
''')

def scan(target):
    converted_ip = check_ip(target)
    print('\n' + '[0] Scanning Target... ' + str(target))
    for port in (21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995, 1234, 1723, 3306, 3389, 4444, 5900, 8080):
        scan_port(converted_ip, port)


def check_ip(ip):
    try:
        IPy.IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def get_banner(s):
    return s.recv(1024)

def scan_port(ip_add, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((ip_add, port))
        try:
            banner = get_banner(sock)
            print('[+] open port ' + str(port) + ' : ' + str(banner.decode().strip('\n')))
        except:
            print('[+] open port ' + str(port))
    except:
        pass
if __name__ == "__main__":
    print('[*] Enter target/s to SCAN ports, split targets with , \nEx: www.google.com, www.name.com, 192.168.0.1')

    targets = input('>>> ')

    if ',' in targets:
        for ip_add in targets.split(','):
            scan(ip_add.strip(' '))
    else:
        scan(targets)

