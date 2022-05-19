import json

user = {
    "id": "IamUser",
    "password": "1234",
    "age": 30,
    "language": ["Python", "Java"]
}

# json encoding
json_data = json.dumps(user)
# json decoding
data = json.loads(json_data)
print(data)

# create json file
with open("user.json", "w", encoding = "utf-8") as file:
    json.dump(user, file, indent = 4)

# REST API
import requests

target = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url = target)

# response (transfrom to Python object)
user_data = response.json()

name_list = []
for user in user_data:
    name_list.append(user['name'])

print(name_list)