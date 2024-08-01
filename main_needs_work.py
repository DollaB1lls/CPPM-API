#################################################################################
# This will be ideally a filter, search, and add application from start to finish
##################################################################################
import subprocess
from pyclearpass import *


#################################################################################
# from ping_location, gets ip address from store location
##################################################################################

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
#host = str("0012-12")
ip_address = ping(host)

if ip_address:
    #This block of code drops the last numbers of the IP
    ip_ad = str(ip_address)
    parts = ip_ad.split('.')
    ip = '.'.join(parts[:3]) + '.'
    ip_filter = ip+"0-255"
    print(f"IP: {ip}")
    print(f"IP going into IP filter: {ip_filter}")

################################################################################
# This part is gonna get tricky bear with me while I figure out what Im doing
##################################################################################

login = ClearPassAPILogin(server="https://ptlcppm2.gopenske.com/api",
                         api_token="",
                         verify_ssl="true")

print("sup")
print()
num = 1

get_ends = ApiLogs.get_insight_endpoint_ip_range_by_ip_range(login, ip_filter)
for ends in get_ends['_embedded']['items']:
    #print(ends)
    mac = ends['mac']
    macfilter = f'{{"mac_address": {{"$contains": "{mac}"}}}}'
    #print()
    
    endpoints = ApiIdentities.get_endpoint(login, filter=macfilter, calculate_count="true", profile_details="True")
    
    for endpoint in endpoints['_embedded']['items']:
        attributes = endpoint.get('attributes', {})
        if attributes.get('Penske Wired CatchAll') == 'true':
            print(f"{num})")
            print(f"MAC: {endpoint['mac_address']} IP: {ends['ip']} ")
            print(f"Category: {ends['device_category']}  Device: {ends['device_family']},{ends['device_name']}")
            print()
            num = num + 1

print("finished")

# print("sup")

# # Fetch all endpoints and store them in a dictionary for faster access later
# all_endpoints = {}
# get_ends = ApiLogs.get_insight_endpoint_ip_range_by_ip_range(login, ip_filter)
# for ends in get_ends['_embedded']['items']:
#     mac = ends['mac']
#     ip = ends['ip']
#     macfilter = f'{{"mac_address": {{"$contains": "{mac}"}}}}'
    
#     endpoints = ApiIdentities.get_endpoint(login, filter=macfilter, calculate_count="true", profile_details="True")
#     all_endpoints[mac] = endpoints['_embedded']['items']

# # Process each endpoint
# for ends in get_ends['_embedded']['items']:
#     mac = ends['mac']
#     endpoints = all_endpoints.get(mac, [])
    
#     for endpoint in endpoints:
#         attributes = endpoint.get('attributes', {})
#         if attributes.get('Penske Wired CatchAll') == 'true':
#             print(f"MAC: {endpoint['mac_address']} Category: {ends['device_category']}  Device: {ends['device_family']},{ends['device_name']}  ")
#             print()

# print("finished")

