import requests

# Tokens By Wallet (POST /:apiKey/assets/tokens/by-address)
response = requests.post(
  "https://api.g.alchemy.com/data/v1/docs-demo/assets/tokens/by-address",
  headers={},
  json={
    "addresses": [
      {
        "address": "0xA9bC66E9244616A38061a1e8E2B9D2A1B85477c4",
        "networks": [
          "eth-mainnet",
          "eth-mainnet"
        ]
      }
    ]
  },
)
print(response.status_code)
print(response.text[:100])
#print(response.json())
