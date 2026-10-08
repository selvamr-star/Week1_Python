import requests

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

print("Status code:", response.status_code)

if response.status_code == 200:
    users = response.json()
    for user in users:
        print(user["name"])
else:
    print("Something went wrong")