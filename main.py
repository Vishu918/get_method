import requests

# Replace 'your_user_id_here' with the actual user ID you want to fetch
user_id_to_fetch = 'your_user_id_here'

# The API endpoint with the user_id
url = f'https://example-api.com/users/{user_id_to_fetch}'

try:
    # Sending GET request to the API
    response = requests.get(url)

    # Checking if the request was successful (status code 200)
    if response.status_code == 200:
        user_data = response.json()  # Assuming the API returns JSON data
        print("User details:")
        print("User ID:", user_data.get("user_id"))
        print("Name:", user_data.get("name"))
        print("Email:", user_data.get("email"))
        # Add other attributes you have stored for the user
    else:
        print("Failed to retrieve user details. Status code:", response.status_code)
except requests.exceptions.RequestException as e:
    print("Error occurred during the request:", e)
