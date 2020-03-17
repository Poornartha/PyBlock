from web3 import Web3

ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

acc1 = "0x5b7BcE49495F6c545d00835B2756D6C3774D657d"
acc2 = "0x273F2Ab6C53fFf4e8f204767d4A170437d138B48"

private_key = "644dad28a6caa4030bcd5c38f3e1086b47a80d1ea523f29fa47102d9412a562e"

# Create Nonce for Tax Count

nonce = web3.eth.getTransactionCount(acc1)

# Create Transaction:

tx = {
    'nonce': nonce,
    'to': acc2,
    'value': web3.toWei(1, 'ether'),
    'gas': 200000,
    'gasPrice': web3.toWei(50, 'gwei'),
}

# Sign Transaction:

sign_txn = web3.eth.account.signTransaction(tx, private_key)

# Get the hash:

hash = web3.eth.sendRawTransaction(sign_txn.rawTransaction)
print(web3.toHex(hash))
