from pyclearpass import *
import json
import requests

login = ClearPassAPILogin(server="https://ptlcppm2.gopenske.com/api",
                         api_token="1fa8c3151145337d2779605a6e61d7d39c2436cd",
                         verify_ssl="true")

print("hello")


ip_filter = '{"ip_address": {"$contains": "3.147.239.115"}}' #doesntwork
attribute = "{'attributes': {'$equals': 'Penske Wired CatchAll': 'true'}}" #doesnwork
statusfilter = '{"status": {"$eq": "known"}}' #works
macfilter = '{"mac_address": {"$contains": "b400169cc1"}}' #works
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

print("finished")


