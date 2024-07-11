#Sample to add whatever to

from pyclearpass import *
import json
import requests

login = ClearPassAPILogin(server="https://ptlcppm2.gopenske.com/api",
                          api_token="",
                          verify_ssl="True")

print("test")