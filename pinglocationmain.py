###########################################################
# Ping store location and then extract IP address - functional
# Created by Devin Dolla        Last modified : 7/2/24
###########################################################

import subprocess

def ping(host):
    # Use subprocess to run the ping command
    result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Check the return code to see if the ping was successful
    if result.returncode == 0:
        print(f"Ping to {host} was successful")
        
        # Splitting lines of output and getting IP address
        lines = result.stdout.splitlines()
        for line in lines:
            if 'Reply from' in line:
                ip_address = line.split()[2][:-1]
                return ip_address
    else:
        print(f"Ping to {host} failed")
        print("##################################################")

print("##################################################")
host = input("Enter store location:")
print("##################################################")
ip_address = ping(host)

if ip_address:
    print("##################################################")
    print(f"The IP address of {host} is: {ip_address}")
    print("##################################################")
    #This block of code drops the last numbers of the IP
    ip_ad = str(ip_address)
    parts = ip_ad.split('.')
    ip_filter = '.'.join(parts[:3]) + '.'
    print(f"The IP going into ClearPass filter: {ip_filter}")
    print("##################################################")
    print()




