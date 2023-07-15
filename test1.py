import hashlib
import json
from time import time


class Blockchain:
    def __init__(self):
        self.chain = []
        self.transactions = []

        # Genesis block
        self.new_block(previous_hash='1')

    def new_block(self, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.transactions,
            'previous_hash': previous_hash
        }
        block['hash'] = self.hash(block)

        self.transactions = []  # Clear transactions after adding them to a block
        self.chain.append(block)
        return block

    @staticmethod
    def hash(block):
        string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]

    def new_transaction(self, sender, receiver, amount):
        transaction = {
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        }
        self.transactions.append(transaction)
        return self.last_block['index'] + 1


blockchain = Blockchain()

t1 = blockchain.new_transaction('Ayush', 'Guna', '5 BTC')
t2 = blockchain.new_transaction('Guna', 'Luigi', '3 BTC')
t3 = blockchain.new_transaction('Luigi', 'Ayush', '2 BTC')

blockchain.new_block(previous_hash='12345')

t4 = blockchain.new_transaction('Guna', 'Ayush', '2 BTC')
t5 = blockchain.new_transaction('Guna', 'Luigi', '3 BTC')
t6 = blockchain.new_transaction('Luigi', 'Guna', '1 BTC')

blockchain.new_block(previous_hash='45678')

t7 = blockchain.new_transaction('Guna', 'Ayush', '4 BTC')
t8 = blockchain.new_transaction('Luigi', 'Guna', '4 BTC')
t9 = blockchain.new_transaction('Luigi', 'Ayush', '2 BTC')

print("Blockchain:", blockchain.chain)
