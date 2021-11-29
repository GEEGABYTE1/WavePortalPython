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

    signed_in = None
    signed_in_user = None

    def interaction(self):
        if self.signed_in == True:
            print("Welcome to Interact! A Simulated Smart Contract Editor ")
            print("/wave: To wave at a user")
            print("/deploy_wave: To deploy a new wave")
            print("/view_waves: To view your waves")        # Print Pass transactions with hashes and datetime, and name
        else:
            pass 

    def prompt(self):
        self.interaction()
        while True:
            prompt = str(input(': '))

            
            if prompt == '/wave':
                wave_validation = None
                chosen_user = str(input("Please type in a user you would like to wave to: "))
                user_validation = None
                accounts = db.find({})
                for account in accounts:
                    account_user = account['Username']
                    if account_user == chosen_user:
                        user_validation = True
                        sender = signed_in_user
                        sender_hash = self.find_user_hash(sender)
                        date_of_wave = datetime.now()
                        transaction_wave = {'Sender': signed_in_user, 'Sender Hash': sender_hash, 'Date': date_of_wave}
                        transaction_hash = blockchain.add_block(transaction_wave)
                        transaction_wave['Wave Hash': transaction_hash]
                        
                        account_transactions_lst = account['Transactions']
                        account_wave_count = account['Transaction_Count']
                        account_transactions_lst.append(transaction_wave)
                        account_wave_count += 1

                        time.sleep(0.1)
                        print(colored("You have successfully wave at {user}".format(user=sender), 'green'))
                        wave_validation = True
                    else:
                        pass 
            
                if wave_validation == None:
                    print(colored('{user} cannot be waved to'.format(user=chosen_user), 'red'))
    
    
    def find_user_hash(self, user):
        accounts = db.find({})
        for account in accounts:
            account_user = account['Username']
            if account_user == user:
                account_hash = account['User_Hash']
                return account_hash


    def transaction(self):
        pass

    def sign_up(self):
        user_user = str(input("Please type in a username: "))
        user_pass = str(input("Please type in a password: "))
        user_pass = user_pass.strip(" ")
        new_user = User()
        new_user = new_user.create_user(user_user, user_pass)
        user_account = {'Username': new_user[0], 'Password': new_user[1], 'Transaction_Count': new_user[2], 'Transactions': new_user[-2], 'User_Hash': new_user[-1]}
        db.insert_one(user_account)
        print(colored("Account creation successful!", 'green'))
        time.sleep(0.2)
        print("{user} account hash: {hash}".format(user=new_user[0], hash=new_user[-1]))

    def sign_in(self):
        user_user = str(input("Please type in your username: "))
        user_pass = str(input("Please type in your password: "))
        user_hash = str(input("Please type in your account hash: "))
        
        users = db.find({})
        
        for account in users:
            current_user = account['Username']
            current_pass = account['Password']
            current_user_hash = account['User_Hash']

            if current_user == user_user and current_pass == user_pass and current_user_hash == user_hash:
                print(colored("You have successfully signed in as {user}".format(user=current_user), 'green'))
                self.signed_in = True
                self.signed_in_user = current_user
            else:
                pass 
        
        if self.signed_in == None:
            print(colored("Some credentials don't match", 'red'))



class User:

    def create_user(self, name, password):
        amount = random.randint(100, 10000)              # Transactions are in dollars
        transactions = 0 
        transactions_lst = []
        time_stamp_of_creation = datetime.datetime.now()
        user_header = str(amount) + str(transactions) + str(time_stamp_of_creation) + password + name
        user_hash = sha256(user_header.encode())
        user_hash = user_hash.hexdigest()

        return name, password, transactions, transactions_lst, user_hash


test = Interact()




