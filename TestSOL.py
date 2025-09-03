import requests
import os

API_KEY = os.getenv("NOWNODES_API_KEY", "69945f5b-b709-4509-864d-fc36c61918f1")
RPC_URL = "https://sol.nownodes.io"

OWNER_ADDRESS = "7VtRDGmSbcTdpaJ22pGEDmUPkPxVGoSCvUaY1TebTHNB"

def get_stake_accounts(owner: str):
    """Возвращает stake-аккаунты для данного владельца (withdraw authority)."""
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getProgramAccounts",
        "params": [
            "Stake11111111111111111111111111111111111111",
            {
                "encoding": "jsonParsed",
                "filters": [
                    {"memcmp": {"offset": 44, "bytes": OWNER_ADDRESS}}
                ]
            }
        ]
    }
    headers = {
        "Content-Type": "application/json",
        "api-key": API_KEY
    }
    r = requests.post(RPC_URL, json=payload, headers=headers, timeout=30)
    r.raise_for_status()
    return r.json()["result"]

def sum_delegated_stake(accounts):
    total = 0
    for acc in accounts:
        try:
            delegated = int(acc["account"]["data"]["parsed"]["info"]["stake"]["delegation"]["stake"])
            total += delegated
        except KeyError:
            continue
    return total / 1e9  # в SOL

if __name__ == "__main__":
    stake_accounts = get_stake_accounts(OWNER_ADDRESS)
    print(f"Найдено stake-аккаунтов: {len(stake_accounts)}")

    total_staked = sum_delegated_stake(stake_accounts)
    print(f"Суммарно делегировано: {total_staked:.9f} SOL")

    # для наглядности выведем по каждому аккаунту
    for acc in stake_accounts:
        pubkey = acc["pubkey"]
        delegated = int(acc["account"]["data"]["parsed"]["info"]["stake"]["delegation"]["stake"])
        print(f"  {pubkey}: {delegated/1e9:.9f} SOL")
