import requests

# Replace 'YOUR_TOKEN_HERE' with your actual token
token = '2f594390472ffd95e8c63817940d7e18e07e06e0'

# URL endpoint you want to make a GET request to
url = 'https://iotapi.pi-innovations.com.np/api/get_led_status'

# Create a headers dictionary with the Authorization token
headers = {'Authorization': f'Token {token}'}

# Make the GET request with headers
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Process the response data
    data = response.json()
    # Do something with the data
    print(data)
else:
    print(f"Failed with status code: {response.status_code}")
