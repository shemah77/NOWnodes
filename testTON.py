import os
import requests

TON_ADDRESS = "UQAIvRGQJyCmtxzXutOKSXxAFxhkSZYcWMx8zF3goM1tBnPA"

# 1) Баланс TON через NOWNodes (возвращает нанотоны)
NOWNODES_API_KEY = os.getenv("NOWNODES_API_KEY", "69945f5b-b709-4509-864d-fc36c61918f1")
NOWNODES_TON_URL = "https://ton.nownodes.io/getAddressBalance"

def ton_balance(address: str) -> float:
    """Возвращает баланс адреса в TON (в SOL-тоннах: TON), переводя из нанотонов."""
    r = requests.get(
        NOWNODES_TON_URL,
        params={"address": address},
        headers={"api-key": NOWNODES_API_KEY, "Accept": "application/json"},
        timeout=20,
    )
    r.raise_for_status()
    print (r.json())
    nano = int(r.json()["result"])  # нанотоны
    return nano / 1_000_000_000  # → TON

# 2) Джеттоны (SPL-аналог) через TON API (TonAPI)
TONAPI_KEY = os.getenv("TONAPI_KEY", "AG3CYHH7LVH6MWQAAAAEGBS5YLWQBVKLQAS2CQWFCYQ7YHWC4L7BYMSPRRMMUDEFRSIHSGY")
TONAPI_BASE = "https://tonapi.io"

def ton_jettons(address: str) -> list[dict]:
    """
    Возвращает список джеттонов на адресе с балансами и метаданными.
    Каждый элемент обычно содержит символ/имя, master, wallet, decimals и amount.
    """
    r = requests.get(
        f"{TONAPI_BASE}/v2/accounts/{address}/jettons",
        headers={"accept": "application/json", "Authorization": f"Bearer {TONAPI_KEY}"},
        timeout=20,
    )
    r.raise_for_status()
    data = r.json()
    return data.get("balances", data)  # у TonAPI поле часто называется balances

if __name__ == "__main__":
    bal = ton_balance(TON_ADDRESS)
    print(f"TON balance: {bal:.9f} TON")

    jettons = ton_jettons(TON_ADDRESS)
    if not jettons:
        print("Jettons: none")
    else:
        print("Jettons:")
        for j in jettons:
            # amount обычно в минимальных единицах → приводим к человекочитаемому формату, если есть decimals
            amt_raw = int(j.get("balance", 0) or j.get("jetton_balance", 0))
            decimals = j.get("jetton", {}).get("decimals") or j.get("decimals") or 9
            ui_amount = amt_raw / (10 ** int(decimals))
            symbol = j.get("jetton", {}).get("symbol") or j.get("symbol") or ""
            name = j.get("jetton", {}).get("name") or j.get("name") or ""
            print(f" - {symbol or name}: {ui_amount}")
