import requests
import os

RPC = "https://eth.nownodes.io"
API_KEY = os.getenv("NOWNODES_API_KEY", "69945f5b-b709-4509-864d-fc36c61918f1")
HEADERS = {"Content-Type": "application/json", "api-key": API_KEY}

OWNER = "0xA9bC66E9244616A38061a1e8E2B9D2A1B85477c4"

TOKENS = {
    # symbol: (contract, decimals)
    "sUSDe": ("0x9D39A5DE30e57443BfF2A8307A4256c8797A3497", 18),
    "USDe":  ("0x4c9EDD5852cd905f086C759E8383e09bff1E68B3", 18),  # оригинальный USDe
    "USDT":  ("0xdAC17F958D2ee523a2206206994597C13D831ec7", 6),
    "USDC":  ("0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48", 6),
    "stETH": ("0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84", 18),
}

def rpc(method, params):
    r = requests.post(RPC, headers=HEADERS,
                      json={"jsonrpc":"2.0","id":1,"method":method,"params":params}, timeout=20)
    r.raise_for_status()
    j = r.json()
    if "error" in j:
        raise RuntimeError(j["error"])
    return j["result"]
# === Новая функция ===
def get_eth_balance(owner: str) -> float:
    """Возвращает нативный баланс ETH в монетах (ETH)."""
    wei_hex = rpc("eth_getBalance", [owner, "latest"])
    return int(wei_hex, 16) / 10**18

def erc20_balance(contract: str, owner: str, decimals: int) -> float:
    selector = "70a08231"  # balanceOf(address)
    owner_hex = owner.lower().replace("0x","").rjust(64,"0")
    data = "0x" + selector + owner_hex
    raw = rpc("eth_call", [{"to": contract, "data": data}, "latest"])
    return int(raw, 16) / (10 ** decimals)

if __name__ == "__main__":
    # ETH баланс
    eth_bal = get_eth_balance(OWNER)
    print(f"ETH: {eth_bal:.18f}")

    # ERC-20 токены
    for sym, (contract, decimals) in TOKENS.items():
        try:
            bal = erc20_balance(contract, OWNER, decimals)
            if bal > 0:
                print(f"{sym}: {bal}")
        except Exception as e:
            print(f"{sym}: error {e}")
