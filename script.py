from blockchain import Blockchain
import datetime 
from hashlib import sha256
from pymongo import MongoClient
from termcolor import colored
import random
import time
from contract import Contract

blockchain = Blockchain()

user_cluster = MongoClient("mongodb+srv://BlindCelery:123@blockchain.uq4dq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = user_cluster['blockchain']['users']


class Interact:

    signed_in = None
    signed_in_user = None

    def __init__(self):
        while True:
            print('\n')
            print('/sign_up: To sign up to the chain')
            print('/sign_in: If you already have a username')
            user_prompt = str(input(": "))
            user_prompt = user_prompt.strip(" ")
            if user_prompt == '/sign_up':
                self.sign_up()
            elif user_prompt == '/sign_in':
                self.sign_in()
                if self.signed_in == True:
                    self.interaction()
                    self.prompt()
            else:
                print(colored("Command not foud!", 'red'))


    def interaction(self):
        if self.signed_in == True:
            print('\n')
            print(colored("Welcome to Interact! A Simulated Smart Contract Editor ", 'blue'))
            print("/wave: To wave at a user")
            print("/view_waves: To view your waves")        # Print Pass transactions with hashes and datetime, and name
        else:
            pass 

    def prompt(self):
        while True:
            prompt = str(input(': '))

            if prompt == '/wave':
                wave_validation = None
                chosen_user = str(input("Please type in the hash of a user you would like to wave to: "))
                user_validation = None
                accounts = db.find({})
                for account in accounts:
                    account_user = account['User_Hash']
                    if account_user == chosen_user:
                        user_validation = True
                        sender = self.signed_in_user
                        sender_hash = self.find_user_hash(sender)
                        date_of_wave = datetime.datetime.now()
                        transaction_wave = {'Sender': self.signed_in_user, 'Sender Hash': sender_hash, 'Date': date_of_wave}
                        transaction_hash = blockchain.add_block(transaction_wave)
                        transaction_wave['Wave Hash'] = transaction_hash
                        
                        account_transactions_lst = account['Transactions']
                        account_wave_count = account['Wave']
                        account_transactions_lst.append(transaction_wave)
                        account_wave_count.add_wave()

                        time.sleep(0.1)
                        sent_user = account['Username']
                        print(colored("{primary} have successfully wave at {user}".format(primary=self.signed_in_user, user=sent_user), 'green'))
                        wave_validation = True
                    else:
                        pass 
            
                if wave_validation == None:
                    print(colored('{user} cannot be waved to'.format(user=chosen_user), 'red'))
            
            elif prompt == '/view_wave':
                chosen_user = str(input("Please type in a hash of a user you would like to see the number of waves: "))
                accounts = db.find({})
                valid = False
                for account in accounts:
                    account_user = account['User_Hash']
                    if account_user == chosen_user:
                        valid = True 
                        account_wave_amount = account['Wave']
                        account_wave_amount = account_wave_amount.wave
                        print("Here are the number of waves of {user}: {wave}".format(user=chosen_user, wave=account_wave_amount))
                        time.sleep(0.2)
                        print("Here are past wave details: ")
                        

    
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
        while True:
            user_user = str(input("Please type in a username: "))
            user_pass = str(input("Please type in a password: "))
            users = self.retrieve_all_users()
            if user_user in users:
                print(colored('That user is already taken', 'blue'))
            else:
                user_pass = user_pass.strip(" ")
                new_user = User()
                new_user = new_user.create_user(user_user, user_pass)
                user_account = {'Username': new_user[0], 'Password': new_user[1], 'Wave': Contract(), 'Transactions': new_user[-2], 'User_Hash': new_user[-1]}
                db.insert_one(user_account)
                print(colored("Account creation successful!", 'green'))
                time.sleep(0.2)
                print("{user} account hash: {hash}".format(user=new_user[0], hash=new_user[-1]))
                break

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

    def retrieve_all_users(self):
        users = []
        accounts = db.find({})
        for account in accounts:
            users.append(account['Username'])
        
        return users



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


interaction_prompt = Interact()






