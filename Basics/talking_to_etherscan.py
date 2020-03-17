from web3 import Web3
import matplotlib.pyplot as plt

# Connect with Infura API
# Infura Url helps you connect to your node and MetaMask will act as an interface.

infura_url = "{Your Infura URL}"
web3 = Web3(Web3.HTTPProvider(infura_url))
print(web3.isConnected())

# Getting Latest Block:
latest = web3.eth.blockNumber
print(latest)

# Connect to the latest block:
print(web3.eth.getBlock(latest))

# Plot Difficulties:
index = []
difficulties = []

# Mapping Blocks difficulties:
print("Recent Block Difficulties: ")
for i in range(10, 0, -1):
    block = web3.eth.getBlock(latest - i)
    print("%d: " % (11-i), end="")
    diff = block.difficulty
    print(diff)
    index.append(i)
    difficulties.append(diff)

# Plot and show:
plt.plot(index, difficulties)
plt.xlabel("Recent Blocks")
plt.ylabel("Difficulties")
plt.show()

# Print Transaction by Transaction Hash:
txn_hash = "0x663833ad15117b16798e67b694becfc9acbf6d018a5ddf50f64ad9ba0da4d8a0"
print(web3.eth.getTransaction(txn_hash))

# Print Block by Block Hash:
block_hash = "0x40218a85c267487bb726cf16acdc95e91b0819fd737f154dad671d4e5eba0ac2"
# Matching Transaction:
print(web3.eth.getTransactionByBlock(block_hash, 186))
# Printing a different transaction:
print(web3.eth.getTransactionByBlock(block_hash, 185))

