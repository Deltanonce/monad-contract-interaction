from web3 import Web3
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access variables
wallet_address = os.getenv('WALLET_ADDRESS')
private_key = os.getenv('PRIVATE_KEY')
contract_address = os.getenv('CONTRACT_ADDRESS')
rpc_url = os.getenv('RPC_URL')

# Connect to Monad Testnet
web3 = Web3(Web3.HTTPProvider(rpc_url))

# ABI of the contract
ABI = [
    {
        "constant": True,
        "inputs": [],
        "name": "greeting",
        "outputs": [{"name": "", "type": "string"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [{"name": "_greeting", "type": "string"}],
        "name": "setGreeting",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
    },
]

# Load contract
contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI)

# Function to read greeting
def get_greeting():
    greeting = contract.functions.greeting().call()
    print(f"Current Greeting: {greeting}")
    return greeting

# Function to update greeting
def set_greeting(new_message):
    nonce = web3.eth.get_transaction_count(WALLET_ADDRESS)

    txn = contract.functions.setGreeting(new_message).build_transaction({
        "from": WALLET_ADDRESS,
        "gas": 300000,
        "gasPrice": web3.to_wei("1", "gwei"),
        "nonce": nonce,
    })

    # Sign and send transaction
    signed_txn = web3.eth.account.sign_transaction(txn, PRIVATE_KEY)
    txn_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

    print(f"Transaction sent: {txn_hash.hex()}")
    return txn_hash.hex()

# Example Usage
if __name__ == "__main__":
    get_greeting()  # Read the greeting
    set_greeting("Hello Monad!")  # Update the greeting


# Example Usage
get_greeting()  # Read the greeting
set_greeting("Hello Monad!")  # Update the greeting

