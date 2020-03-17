from web3 import Web3

# Consider your user does not have an Etherium Account
# So you'd have to create an account on his behalf.
# To Do this:

# Step 1. Connect your account:
infura_url = "{Your Infura URL}"
web3 = Web3(Web3.HTTPProvider(infura_url))

# Create an account for your user:
account = web3.eth.account.create()


# Encrypt the account as you don't want anyone to know the private key:
# You'd need a password to access the decrypted keystore value:
keystore = account.encrypt('admin')

# In order to retrieve the account:
web3.eth.account.decrypt(keystore, 'admin')

# To transact - Refer to transact.py:
account.signTransaction()

