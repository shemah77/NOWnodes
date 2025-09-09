import requests



if __name__ == "__main__":
    API_KEY = "2f59e40b-df01-4f10-b07b-a98331b34441"
    ACCOUNT = "7VtRDGmSbcTdpaJ22pGEDmUPkPxVGoSCvUaY1TebTHNB"
    url = f"https://mainnet.helius-rpc.com/?api-key={API_KEY}"
    payload = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "getBalance",
    "params": [ACCOUNT]}
    resp = requests.post(url, json=payload).json()
    print(resp)







