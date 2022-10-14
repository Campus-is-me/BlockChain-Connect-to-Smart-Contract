import http
import json 
from web3 import Web3

from web3 import EthereumTesterProvider
infura_url = 'https://mainnet.infura.io/v3/1e1c0742bfc64e6483a320b0547fcae9'
web3 = Web3(Web3.HTTPProvider(infura_url))
print(web3.isConnected())
print(web3.eth.blockNumber)

#create wallet 
i = 0
while i < 100:
    account = web3.eth.account.create()
    address = account.address
    private_key = account.privateKey
    print(f"{address}:{private_key.hex()}")
    i+=1 
