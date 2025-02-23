---

# **Monad Contract Interaction**

This Python script facilitates interaction with a smart contract deployed on the **Monad Testnet** using `web3.py`.

## **🚀 Features**
- ✅ Read the current greeting message from the contract.
- ✅ Update the greeting message with a new one.

## **🛠 Prerequisites**
- Python **3.x**
- `web3.py` library
- `python-dotenv` library

## **📥 Installation**

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Deltanonce/monad-contract-interaction.git
   cd monad-contract-interaction
   ```

2. **Install Dependencies**:

   ```bash
   pip install web3 python-dotenv
   ```

## **🔧 Configuration**
Before running the script, create a `.env` file in the project directory to securely store your credentials:

```ini
WALLET_ADDRESS=your_wallet_address
PRIVATE_KEY=your_private_key
CONTRACT_ADDRESS=your_contract_address
RPC_URL=https://testnet-rpc2.monad.xyz/
```

## **📌 Usage**
Run the script to interact with the smart contract:

```bash
python monad_contract_interaction.py
```

## **⚠️ Security Notice**
🚨 **Never expose your private key in public repositories!**  
Use environment variables (`.env` file) and **never** hardcode sensitive information in your script.

---

