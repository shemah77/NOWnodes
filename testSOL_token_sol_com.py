#!/usr/bin/env python3
"""
Solana Cookbook - How to Get a Token Account's Balance
"""

import asyncio
from solana.rpc.async_api import AsyncClient
from solders.pubkey import Pubkey


async def main():
    rpc = AsyncClient("https://api.mainnet-beta.solana.com")

    # Use a real token account address from mainnet
    token_account_address = Pubkey.from_string("7VtRDGmSbcTdpaJ22pGEDmUPkPxVGoSCvUaY1TebTHNB")

    async with rpc:
        try:
            balance = await rpc.get_token_account_balance(token_account_address)
            print(balance)
        except Exception as e:
            print(f"Error getting token balance: {e}")
            print("This might be because the account doesn't exist or isn't a token account")


if __name__ == "__main__":
    asyncio.run(main())