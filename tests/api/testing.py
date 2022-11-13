import requests

url = 'http://127.0.0.1:8000/api/v1/users/1/'
data = {"phone_number":"0944194927","password":"Nguyen123@"}
response = requests.get(url)
# self.assertEquals(response.data["phone_number"], data["phone_number"])
print("Day la response: ", response)