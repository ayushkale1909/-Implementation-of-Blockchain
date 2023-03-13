import hashlib 
import json
from time import time 

class Blockchain(object):
   def __init__(self):
      self.chain=[]
      self.transactions = []
      
      self.new_block(previous_hash="Hello World",proof = 100)

   def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain)+1,
            'timestamp': time(),
            'transactions':self.transactions,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.transactions= []
        self.chain.append(block)
        return block

   @property
   def last_block(self):
    return self.chain[-1]
    
    
   def new_transaction(self, sender, reciever, amount):
    transaction= {
        'sender': sender,                
        'reciever': reciever,
        'amount': amount
    }
    self.transactions.append(transaction)
    return self.last_block['index'] +1
        
   def hash(self, block):
        string = json.dumps(block,sort_keys = True)
        block_string = string.encode()
        hash_sha256 = hashlib.sha256(block_string)
        hash_output = hash_sha256.hexdigest()
        return hash_output


blockchain = Blockchain()
t1 = blockchain.new_transaction('Ayush','Guna', '5 BTC')
t2 = blockchain.new_transaction('Guna', 'Luigi','3 BTC')
t3 = blockchain.new_transaction('Luigi','Ayush','2 BTC')

blockchain.new_block(12345)
t4 = blockchain.new_transaction('Guna','Ayush', '2 BTC')
t5 = blockchain.new_transaction('Guna', 'Luigi','3 BTC')
t6 = blockchain.new_transaction('Luigi','Guna','1 BTC')

blockchain.new_block(45678)

t7 = blockchain.new_transaction('Guna','Ayush', '4 BTC')
t8 = blockchain.new_transaction('Luigi','Guna','4 BTC')
t9 = blockchain.new_transaction('Luigi','Ayush','2 BTC')


print("Blockchain:   ", blockchain.chain)
