##########################################################################
#Ping store location
##########################################################################

import subprocess

def ping(host):
    # Run ping command
    result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE,text=True)
    
    # Check the return code to see if the ping was successful
    if result.returncode == 0:
        print(f"Ping to {host} was successful!")
        print(result.stdout)
    else:
        print(f"Ping to {host} failed!")
        print(result.stderr)

# Enter store location and run fxn
#location = input("Enter store location: ")
location = "0022-10"
ping(location)


