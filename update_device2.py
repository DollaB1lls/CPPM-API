
from pyclearpass import ClearPassAPI

# Initialize the ClearPass API client
client = ClearPassAPI(
    server='https://clearpass-server-url',
    client_id='demo',
    client_secret='dMbvaEFUvifGQEUAv9Jk8UW+GISwMKs5HHuZCmremejx',
    grant_type='client_credentials'  # Assuming OAuth2 client credentials flow
)

# Authenticate with ClearPass
client.login()

# Function to update a device by IP address
def update_device_by_ip(device_ip, new_description):
    try:
        # Retrieve the device by IP address
        device_query = client.api_request('GET', 'endpoint', params={'filter': f"ip_address='{device_ip}'"})
        
        # Check if the device exists
        if device_query.get('count', 0) > 0:
            device_id = device_query['items'][0]['id']
            
            # Update the device's description
            update_data = {
                'description': new_description
            }
            
            client.api_request('PUT', f'endpoint/{device_id}', data=update_data)
            print("Device updated successfully.")
        else:
            print("Device not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
device_ip = '192.168.1.100'
new_description = 'Updated Device Name'
update_device_by_ip(device_ip, new_description)
