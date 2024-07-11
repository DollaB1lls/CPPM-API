

from pyclearpass import *
import json
import requests
import dicttoxml

login = ClearPassAPILogin(server="https://ptlcppm2.gopenske.com/api",
                          api_token="1fa8c3151145337d2779605a6e61d7d39c2436cd",
                          verify_ssl="True")
headers = {
    "accept": "application/json"
}

elements = (ApiPolicyElements.get_role(login, limit=50 )) 
#print(elements)
for element in elements["_embedded"]["items"]:
    print(element)
    print(f"ID: {element['id']}  Name: {element['name']}")
    print(f"Desc: {element['description']}")
    print()
    pass

#print(ApiLogs.get_insight_endpoint_ip_by_ip(login,ip="3.147.136.162"))
#elements2 = ApiIdentities.get_api_client()
#print(elements2)


#ip = input("Enter IP range:")
ip = "3.145.96.0-255"

get_ends = ApiLogs.get_insight_endpoint_ip_range_by_ip_range(login,ip)

#print(get_end)
for ends in get_ends['_embedded']['items']:
    print(ends)
    print(f"MAC: {ends['mac']}   IP: {ends['ip']}     Category: {ends['device_category']}  Device: {ends['device_family']},{ends['device_name']}  ")
    print()
    pass


##Convert data to xml and save

# xml_data = dicttoxml(get_end)
# xml_filename = "data.xml"
# with open(xml_filename, "wb") as xml_file:
#     xml_file.write(xml_data)
# print(f"XML data saved to {xml_filename}")

