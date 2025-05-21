import requests
response= requests.get ("https://api.github.com/users/octocat")
print(response.status_code)
print(response.text)
print(response.json())

