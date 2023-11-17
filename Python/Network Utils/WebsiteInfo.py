from colorama import Fore, Style
import ctypes
import socket
import time

vulnerable_ports = {
    21: "(FTP)",
    22: "(SSH)",
    23: "(Telnet)",
    25: "(SMTP)",
    53: "(DNS)",
    80: "(HTTP)",
    110: "(POP3)",
    135: "(RPC)",
    139: "(NetBIOS)",
    143: "(IMAP)",
    443: "(HTTPS)",
    445: "(SMB)",
    1433: "(MSSQL)",
    1521: "(Oracle Database)",
    3306: "(MySQL)",
    3389: "(RDP)",
    5432: "(PostgreSQL)",
    5900: "(VNC)",
}

def set_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)
    
url_list = input("Enter URLs (comma-separated): ").split(',')
sstart_tajm = time.time()
set_title(f"Illegal Network - Website Info v.1.0")
for url in url_list:
    start_time = time.time()

    try:
        ip_address = socket.gethostbyname(url)

        with open(f'url-({ip_address})({url}).txt', 'w') as file:
            file.write(f"IP address for {url}: {ip_address}\n")

            dns_info = socket.gethostbyname_ex(url)
            file.write(f"\nDNS information for {url}:")
            file.write(f"\nHostname: {dns_info[0]}")
            file.write(f"\nAliases: {dns_info[1]}")
            file.write(f"\nIP addresses: {dns_info[2]}\n")

            for port in range(1, 1025):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.1)
                result = sock.connect_ex((ip_address, port))
                if result == 0:
                    port_sc = vulnerable_ports.get(port, "")
                    file.write(f"\nPort: {port} {port_sc} (Open)")
                    sock.close()
                else:
                    sock.close()

            file.write(f"\n\n")

        end_time = time.time() - start_time
        print(f"Done in {Fore.GREEN + Style.BRIGHT}{end_time:.2f}{Fore.RESET + Style.RESET_ALL} seconds for {url}")

    except socket.gaierror as e:
        print(f"Error resolving {url}: {str(e)}")

eend_time = time.time() - sstart_tajm
print(f"All executed in {Fore.GREEN + Style.BRIGHT}{eend_time:.2f}{Fore.RESET + Style.RESET_ALL}s")
