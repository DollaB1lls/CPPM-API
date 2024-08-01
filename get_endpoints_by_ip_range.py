# This program is supposed takes the ip adress and returns a list of items within that IP range

from pyclearpass import *
import json
import requests
import dicttoxml

login = ClearPassAPILogin(server="https://ptlcppm2.gopenske.com/api",
                          api_token="",
                          verify_ssl="True")
headers = {
    "accept": "application/json"
}

#print(ApiLogs.get_insight_endpoint_ip_by_ip(login,ip="3.147.136.162"))
#elements = ApiIdentities.get_api_client()
#print(elements)

#ip = input("Enter IP range:")
ip = "3.146.33.0-255"

get_ends = ApiLogs.get_insight_endpoint_ip_range_by_ip_range(login,ip)

#print(get_ends)

for ends in get_ends['_embedded']['items']:
    print(ends)
    print(f"MAC: {ends['mac']}   IP: {ends['ip']}     Category: {ends['device_category']}  Device: {ends['device_family']},{ends['device_name']}  ")
    print()
    pass


##Converts data to xml file and saves

# xml_data = dicttoxml(get_end)
# xml_filename = "data.xml"
# with open(xml_filename, "wb") as xml_file:
#     xml_file.write(xml_data)
# print(f"XML data saved to {xml_filename}")

