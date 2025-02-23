from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

RPC_URL = os.getenv("RPC_URL")
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")

print("Loaded environment variables.")

if not all([RPC_URL, WALLET_ADDRESS, PRIVATE_KEY, CONTRACT_ADDRESS]):
    raise ValueError("Missing required environment variables")

web3 = Web3(Web3.HTTPProvider(RPC_URL))
print("Connecting to Monad Testnet...")
if not web3.is_connected():
    raise ConnectionError("Failed to connect to Monad Testnet")
print("Successfully connected to Monad Testnet.")

ABI = [
    {
        "inputs": [],
        "name": "greeting",
        "outputs": [{"name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"name": "_greeting", "type": "string"}],
        "name": "setGreeting",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
]

contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI)
print("Smart contract instance created.")

def get_greeting():
    print("Fetching current greeting...")
    greeting = contract.functions.greeting().call()
    print("Current greeting:", greeting)
    return greeting

def set_greeting(new_message):
    print("Setting new greeting to:", new_message)
    nonce = web3.eth.get_transaction_count(WALLET_ADDRESS)
    print("Current nonce:", nonce)
    txn = contract.functions.setGreeting(new_message).build_transaction({
        "from": WALLET_ADDRESS,
        "gas": 300000,
        "gasPrice": web3.to_wei("1", "gwei"),
        "nonce": nonce,
    })
    print("Transaction built:", txn)
    signed_txn = web3.eth.account.sign_transaction(txn, PRIVATE_KEY)
    print("Transaction signed.")
    txn_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print("Transaction sent. Hash:", txn_hash.hex())
    return txn_hash.hex()

if __name__ == "__main__":
    print("Starting contract interaction...")
    print("Current Greeting:", get_greeting())
    print("Transaction Hash:", set_greeting("Hello Monad!"))


