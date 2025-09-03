import json
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
    print(r.json())
    return r.json()["result"]

def sum_delegated_stake(accounts):
    total = 0
    for acc in accounts:
        try:
            lamports = int(acc["account"]["lamports"])
            total += lamports
        except KeyError:
            continue
    return total / 1e9  # в SOL

def sol_wallet_balance(account):
    # URL эндпоинта
    url = "https://sol.nownodes.io"

    # Заголовки запроса
    headers = {
        'Content-Type': 'application/json',
        'api-key': API_KEY
    }

    # Тело запроса (данные)
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getAccountInfo",
        "params": [
            account,
            {
                "encoding": "base58"
            }
        ]
    }

    try:
        # Выполнение POST-запроса
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()  # Проверка на наличие HTTP-ошибок
        balance = (
            response.json()
            .get("result", {})
            .get("value", {})
            .get("lamports")
        )
        return f"{balance/1e9:.9f}"

        # Печать ответа от сервера в формате JSON
        return response.json()

    except requests.exceptions.RequestException as e:
        return print(f"Произошла ошибка при выполнении запроса: {e}")


if __name__ == "__main__":
    stake_accounts = get_stake_accounts(OWNER_ADDRESS)
    print(f"Найдено stake-аккаунтов: {len(stake_accounts)}")

    total_staked = sum_delegated_stake(stake_accounts)
    print(f"Суммарно в стейкинге : {total_staked:.9f} SOL")

    # для наглядности выведем по каждому аккаунту
    for acc in stake_accounts:
        pubkey = acc["pubkey"]
        delegated = int(acc["account"]["data"]["parsed"]["info"]["stake"]["delegation"]["stake"])
        print(f"  {pubkey}: {delegated/1e9:.9f} SOL")
        balance = sol_wallet_balance(OWNER_ADDRESS)
        print(f' Баланс кошелька {OWNER_ADDRESS}  {balance} SOL')
        total = float(total_staked) + float(balance)
        print(f'total wallet : {total}')






