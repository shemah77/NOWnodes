#!/usr/bin/env python3
"""
Solana Cookbook - How to Get All Token Accounts by Owner
"""

import asyncio
from solana.rpc.async_api import AsyncClient
from solders.pubkey import Pubkey
from spl.token.constants import TOKEN_PROGRAM_ID
from solana.rpc.types import TokenAccountOpts

async def main():
    rpc = AsyncClient("https://api.mainnet-beta.solana.com")

    # Example owner address
    owner = Pubkey.from_string("7VtRDGmSbcTdpaJ22pGEDmUPkPxVGoSCvUaY1TebTHNB")

    async with rpc:
        try:
            # Get all token accounts by owner
            response = await rpc.get_token_accounts_by_owner(
                owner,
                TokenAccountOpts(program_id=TOKEN_PROGRAM_ID)
            )

            print(f"Owner: {owner}")
            print(f"Found {len(response.value)} token accounts:\n")

            for account_info in response.value:
                print(f"Pubkey: {account_info.pubkey}")
                print(f"Owner: {account_info.account.owner}")
                print(f"Lamports: {account_info.account.lamports}")
                print(f"Data Length: {len(account_info.account.data)} bytes")
                print("=" * 50)

        except Exception as e:
            print(f"Error getting token accounts: {e}")

if __name__ == "__main__":
    asyncio.run(main())