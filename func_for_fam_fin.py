import time

import requests

API_KEY = "2f59e40b-df01-4f10-b07b-a98331b34441"  # возьмите из dashboard.helius.dev
RPC_URL = f"https://mainnet.helius-rpc.com/?api-key={API_KEY}"
WITHDRAWER = "7VtRDGmSbcTdpaJ22pGEDmUPkPxVGoSCvUaY1TebTHNB"

def get_stake_accounts(owner: str, api_key: str, url_secret_api_key: str):
    """Возвращает stake-аккаунты для данного withdraw authority"""
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getProgramAccounts",
        "params": [
            # Stake program
            "Stake11111111111111111111111111111111111111",
            {
                "encoding": "jsonParsed",
                "filters": [
                    {
                        "memcmp": {
                            "offset": 44,        # смещение withdraw authority
                            "bytes": owner       # ваш pubkey
                        }
                    }
                ]
            }
        ]
    }

    headers = {"Content-Type": "application/json"}
    url = f"{url_secret_api_key}{api_key}"
    r = requests.post(url, json=payload, headers=headers, timeout=30)
    r.raise_for_status()
    data = r.json()
    return data["result"]

def get_balance(owner: str, api_key: str, url_secret_api_key: str):
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getBalance",
        "params": [owner]}
    url = f"{url_secret_api_key}{api_key}"
    resp = requests.post(url, json=payload).json()
    return resp

def get_SOL_wallet(owner: str, api_key: str, url_secret_api_key: str):
    accounts = get_stake_accounts(owner, api_key, url_secret_api_key)
    print(f"Найдено stake-аккаунтов: {len(accounts)}")
    sum_sol_staking = 0
    for acc in accounts:
        print(acc)
        pubkey = acc["pubkey"]
        lamports = acc["account"]["lamports"]
        sol = lamports / 1_000_000_000
        print(f" Стейкинг  {pubkey}: {sol:.9f} SOL")
        sum_sol_staking += sol
        time.sleep(1)
    print (sum_sol_staking)
    time.sleep(1)
    res = get_balance(owner, api_key, url_secret_api_key)
    sol_balance = res['result']['value'] / 1_000_000_000
    print(f'Баланс {sol_balance:.9f}')
    print(f'Total balance sol: {(sol_balance + sum_sol_staking):.9f}')
    return (sol_balance+sum_sol_staking)

if __name__ == '__main__':
    a = get_SOL_wallet("7VtRDGmSbcTdpaJ22pGEDmUPkPxVGoSCvUaY1TebTHNB",
                   api_key="2f59e40b-df01-4f10-b07b-a98331b34441",
                   url_secret_api_key="https://mainnet.helius-rpc.com/?api-key="
                   )
    print (f' ===============БАЛАНС   ====================  {a}')
