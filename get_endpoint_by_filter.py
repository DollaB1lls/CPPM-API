# This program is supposed to be able to filter endpoints by specific parameters
# WIP - still doesnt do exactly what I want it to do

from pyclearpass import *
from apiclient import APIClient
import json
import requests

login = ClearPassAPILogin(server="https://ptlcppm2.gopenske.com/api",
                         api_token="",
                         verify_ssl="true")

print("hello")

# These are the different filters I have tried, they need to be JSON filter expression
ip_filter = '{"ip_address": {"$contains": "3.147.239.115"}}' #doesntwork
attribute = "{'attributes': {'$equals': 'Penske Wired CatchAll': 'true'}}" #doesnwork
statusfilter = '{"status": {"$eq": "known"}}' #works
macfilter = '{"mac_address": {"$contains": "56a40e4ac534"}}' #works
devicefilter = '{"device_category": {"$contains": "printer"}}'

endpoints = ApiIdentities.get_endpoint(login,filter=macfilter, calculate_count="true",profile_details="True")
#print(endpoints)

for ends in endpoints['_embedded']['items']:
    print()
    print(ends)
    print()
    print(ends['attributes'])
    print()
    pass

# for ends in endpoints['_embedded']['items']:
#     attributes = ends.get('attributes', {})

#     if attributes.get('Penske Wired CatchAll') == 'true':
#         print()
#         print("test2")
#         print(ends)
#         print()
#         print(attributes)
#         print()



print("finished")


