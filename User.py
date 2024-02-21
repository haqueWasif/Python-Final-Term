import random 

class User:
    def __init__(self, name, email, address, password, account_type, bank):
        self.__name = name
        self.__email = email
        self.__address = address
        self.__password = password
        self.__type = account_type
        self.__bank = bank
        self.__balance = 0
        self.__account_num = random.randint(1, 100)
        self.__transaction_history = []
        self.__loans = {self.__bank.name : 0}
        self.__loan_feature = True
        bank.user_accounts = self
    
    
    def __repr__(self) -> str:
        return f'{self.__name}'
    
    def deposit(self, amount):
        self.__balance += amount
        self.__bank.balance = +amount
        
        self.__transaction_history.append({"Deposited" : amount})
    
    def withdraw(self, amount):
        if amount > self.__balance:
            print('Withdrawal amount exceeded')
        else:
            if self.__bank.balance < self.__balance:
                print('Bank is bankrupt')
            else:
                self.__balance -= amount
                self.__bank.balance = -amount
                self.__transaction_history.append({"Withdrawal" : amount})

    @property
    def name(self):
        return self.__name
    
    @property
    def account_type(self):
        return self.__type
    
    @property 
    def bank(self):
        return self.__bank
    
    @property
    def balance(self):
        return self.__balance
    
    @property
    def transaction_history(self):
        return self.__transaction_history
    
    @property
    def get_info(self):
        return self.__name, self.__email, self.__password, self.__type, self.__bank.name

    @property
    def loan_info(self):
        return self.__loans
    
    def loan_feature(self, value):
        self.__loan_feature = value
    
    def take_loan(self, amount):
        if self.__loan_feature:
            if self.__loans[self.__bank.name] < 2:
                if amount <= self.__bank.balance and amount <= self.__bank.balance:
                    print('Your loan request was succesfully completed!')

                    self.__balance += amount
                    self.__bank.balance = -amount
                    self.__bank.loans = amount

                    self.__loans[self.__bank.name] += 1

                    self.__transaction_history.append({"Deposited" : amount})
                
                elif amount == self.__balance and amount > self.__bank.balance:
                    print('Bank is bankrupt')
                
                else:
                    print('Sorry amount is too large to be given as loan')
                return
            else:
                print('Sorry you do not meet the requirements for taking loan')
            return

        print('Sorry you do not meet the requirements for taking loan')        
       

    def transfer_amount(self, user):
        if user.name == self.__name:
            return
        
        amount = self.__balance
        self.withdraw(amount)
        user.deposit(amount)
            

    

    