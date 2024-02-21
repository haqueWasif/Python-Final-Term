class Bank:
    def __init__(self, name):
        self.name = name
        self.__balance = 0
        self.__loans = 0
        self.__users = []
        self.__admin = []
        self.__is_bankrupt = False

    @property
    def user_accounts(self):
        return self.__users
    
    @user_accounts.setter
    def user_accounts(self, user):
        self.__users.append(user)

    @property
    def admin_accounts(self):
        return self.__admin
    
    @admin_accounts.setter
    def admin_accounts(self, admin):
        self.__admin.append(admin)

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        self.__balance += amount
        
    @property
    def loans(self):
        return self.__loans
    
    @loans.setter
    def loans(self, amount):
        self.__loans += amount

    @property
    def bankrupt(self):
        return self.__is_bankrupt

    @bankrupt.setter
    def bankrupt(self, value):
        self.__is_bankrupt = True        


class Admin:
    def __init__(self, name, email, address, password, bank):
        self.__name = name
        self.__email = email
        self.__address = address
        self.__password = password
        self.__bank = bank
        bank.admin_accounts = self
    
    def delete_account(self, user):
        if user.bank.name == self.__bank.name:
            self.__bank.user_accounts.remove(user)
            del user

    def view_accounts(self):
        return self.__bank.user_accounts

    def check_bank_balance(self):
        return self.__bank.balance
    
    def check_bank_loans(self):
        return self.__bank.loans
    
    def set_loan_feature(self, user, value):
        user.loan_feature(value)

    
    @property
    def get_info(self):
        return self.__name, self.__email, self.__password,  self.__bank.name
