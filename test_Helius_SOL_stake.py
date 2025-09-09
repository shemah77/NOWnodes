import time

import requests

API_KEY = "2f59e40b-df01-4f10-b07b-a98331b34441"  # возьмите из dashboard.helius.dev
RPC_URL = f"https://mainnet.helius-rpc.com/?api-key={API_KEY}"

def get_stake_accounts(owner: str):
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
    r = requests.post(RPC_URL, json=payload, headers=headers, timeout=30)
    r.raise_for_status()
    data = r.json()
    return data["result"]

def get_balance(owner: str):
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getBalance",
        "params": [owner]}
    resp = requests.post(RPC_URL, json=payload).json()
    return resp



if __name__ == "__main__":
    withdrawer = "7VtRDGmSbcTdpaJ22pGEDmUPkPxVGoSCvUaY1TebTHNB"  # замените на ваш адрес
    accounts = get_stake_accounts(withdrawer)

    print(f"Найдено stake-аккаунтов: {len(accounts)}")
    sum_sol = 0
    for acc in accounts:
        print (acc)
        pubkey = acc["pubkey"]
        lamports = acc["account"]["lamports"]
        sol = lamports / 1_000_000_000
        print(f" Стейкинг  {pubkey}: {sol:.9f} SOL")
        sum_sol += sol
        time.sleep(1)
    res = get_balance(withdrawer)
    sol_balance = res['result']['value']/1_000_000_000
    print(f'Баланс {sol_balance:.9f}')
    print(f'Total balance sol: {(sol_balance+sum_sol):.9f}')
    RPC_URL = f"https://mainnet.helius-rpc.com/?api-key="
    RPC_URL = f"{RPC_URL}{API_KEY}"
    print (RPC_URL)









