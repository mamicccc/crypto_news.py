import requests

url = "https://cryptopanic.com/api/v1/posts/?auth_token=demo&currencies=BTC"
response = requests.get(url).json()

print("Latest Crypto News:")
for post in response["results"][:5]:
    print("-", post["title"])
