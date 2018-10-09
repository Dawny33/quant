import requests

url = 'https://www.amfiindia.com/spages/NAVAll.txt'

response = requests.get(url=url)

print(response.text)