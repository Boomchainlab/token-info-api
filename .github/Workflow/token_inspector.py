import requests

DUNE_API_KEY = "sim_iCMynyKsMo4g6qSp8oz9xuTQjQfegv4P"
BASE_CHAIN_ID = "8453"
DUNE_ENDPOINT = "https://api.sim.dune.com/v1/evm/token-info"

def fetch_token_info(token_address: str, chain_id: str = BASE_CHAIN_ID):
    """Fetch token metadata from Dune Sim API for the given EVM address."""
    url = f"{DUNE_ENDPOINT}/{token_address}"
    headers = {"X-Sim-Api-Key": DUNE_API_KEY}
    params = {"chain_ids": chain_id}
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"[ERROR] Failed to fetch token info: {e}")
        return None

def print_token_summary(token_data: dict):
    """Prints selected token metadata for review."""
    if not token_data:
        print("No data available.")
        return

    data = token_data.get('data', {})
    print("\n📊 Token Summary:")
    print(f"Name: {data.get('name')}")
    print(f"Symbol: {data.get('symbol')}")
    print(f"Decimals: {data.get('decimals')}")
    print(f"Total Supply: {data.get('total_supply')}")
    print(f"Address: {data.get('address')}")
    print(f"Chain ID: {data.get('chain_id')}")
    print(f"Is Verified: {data.get('is_verified')}")

if __name__ == "__main__":
    # Example Base token
    token_address = "0x233dF63325933fA3f2dac8E695Cd84bb2f91aB07"
    token_info = fetch_token_info(token_address)
    print_token_summary(token_info)
