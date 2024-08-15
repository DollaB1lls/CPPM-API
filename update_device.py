from pyclearpass import *


client = ClearPassAPILogin(
    server='https://ptlcppm2.gopenske.com/api',
    api_token="15bf18a3625adc716f42f4475545e9b6c0e2381d",
    verify_ssl="true"
)
# client = ClearPassAPILogin(
#     server='https://ptlcppm2.gopenske.com/api',
#     client_id='demo',
#     client_secret='dMbvaEFUvifGQEUAv9Jk8UW+GISwMKs5HHuZCmremejx'
# )

# Example: Retrieve a device by IP address
device_ip = '3.144.188.2'
device_query = client.get('endpoint', params={'filter': f"ip_address='{device_ip}'"})

# Check if the device exists
if device_query['count'] > 0:
    device_id = device_query['items'][0]['id']
    
    # Example: Update the device's name
    update_data = {
        'description': 'Updated Device Name'
    }
    
    client.put(f'endpoint/{device_id}', data=update_data)
    print("Device updated successfully.")
else:
    print("Device not found.")
