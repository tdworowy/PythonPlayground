import hashlib
import json
from time import time


class Blockchain:
    def __init__(self):
        self.chain = []
        self.transactions = []

        self.add_block(previous_hash=1,proof=100)

    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def hash(block):
        block_string = json.dumps(block,sort_keys=True).encode()
        return hashlib.sha512(block_string).hexdigest()

    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha512(guess).hexdigest()
        return guess_hash[:4] == "0000"


    def add_block(self, proof, previous_hash=None):
        block={
            'index': len(self.chain)+1,
            'timestamp':time(),
            'transactions':self.transactions,
            'proof':proof,
            'previous_hash':previous_hash or self.hash(self.chain[-1])
        }
        self.transactions = []
        self.chain.append(block)
        return block

    def add_transaction(self,sender,recipient,amount):
        self.transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount':amount,
        })
        return self.last_block['index']+1


    def proof_of_work(self,last_proof):
        proof = 0
        while self.valid_proof(last_proof,proof) is False:
            proof +=1
        return proof

