from blockchain import Blockchain
import datetime 
from hashlib import sha256
from pymongo import MongoClient
from termcolor import colored
import random

blockchain = Blockchain()

user_cluster = MongoClient("mongodb+srv://BlindCelery:123@blockchain.uq4dq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = user_cluster['blockchain']['users']


class Interact:


    
    def transaction(self):
        pass

    def sign_up(self):
        user_user = str(input("Please type in a username: "))
        user_pass = str(input("Please type in a password: "))
        user_pass = user_pass.strip(" ")
        new_user = User()
        new_user = new_user.create_user(user_user, user_pass)
        user_account = {'Name': new_user[0], 'Transactions': new_user[2], 'User_Hash': new_user[-1]}
        db.insert_one(user_account)
        print(colored("Account creation successful!", 'green'))

class User:

    def create_user(self, name, password):
        amount = random.randint(100, 10000)              # Transactions are in dollars
        transactions = 0 
        time_stamp_of_creation = datetime.datetime.now()
        user_header = str(amount) + str(transactions) + str(time_stamp_of_creation) + password + name
        user_hash = sha256(user_header.encode())
        user_hash = user_hash.hexdigest()

        return name, password, transactions, user_hash


test = Interact()

print(test.sign_up())

