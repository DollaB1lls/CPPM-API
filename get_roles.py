# Returns roles of users in CPPM

from pyclearpass import *
import json
import requests

login = ClearPassAPILogin(server="https://ptlcppm2.gopenske.com/api",
                         api_token="1fa8c3151145337d2779605a6e61d7d39c2436cd",
                         verify_ssl="true")

print("hello")

elements = (ApiPolicyElements.get_role(login, limit=50 )) 
#print(elements)
for element in elements["_embedded"]["items"]:
    print(element)
    print(f"ID: {element['id']}  Name: {element['name']}")
    print(f"Desc: {element['description']}")
    print()

