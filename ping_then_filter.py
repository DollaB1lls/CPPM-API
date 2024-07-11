# This will eventually step through all tasks to find ip, filter data, and maybe create mapping rules all in one program
# WIP - need to make mapping rule API stuff 

import subprocess

def ping(host):
    # Use subprocess to run the ping command
    result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Check the return code to see if the ping was successful
    if result.returncode == 0:
        # Splitting lines of output and getting IP address
        lines = result.stdout.splitlines()
        for line in lines:
            if 'Reply from' in line:
                ip_address = line.split()[2][:-1]
                return ip_address
    else:
        print(f"Ping to {host} failed")

host = input("Enter store location:")
ip_address = ping(host)

if ip_address:
    #This block of code drops the last numbers of the IP
    ip_ad = str(ip_address)
    parts = ip_ad.split('.')
    ip_filter = '.'.join(parts[:3]) + '.'
    print(f"IP: {ip_filter}")
    print()