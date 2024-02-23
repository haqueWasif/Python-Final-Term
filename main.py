from User import User
from Bank import Admin, Bank

def main():

    bank_list = [Bank('Brac Bank'), Bank('Agrani Bank')]

    while True:
        print('-------Welcome to Our Bank Management System--------')
        print('1.User\n2.Admin')

        option = int(input('Enter your choice: '))
        
        current_account = None

        if option == 1:
            print('\n---Welcome to the user portal-----')
            print('1.Create new account\n2.Login')

            option = int(input('Enter your choice: '))

            if option == 1:
                print('\n# Please enter the following information for creating an account #')

                name = input('Name: ')
                email = input('Email: ')
                password = input('Password: ')
                address = input('Address: ')
                account_type = input('Account Type (type Savings or Current): ')
                bank_name = input('Bank (type Bank name from the available Banks in the list ex: Brac Bank): ')

                bank_found = False
                for bank in bank_list:
                    if(bank.name == bank_name):
                        user = User(name, email, address, password, account_type, bank)
                        current_account = user
                        bank_found = True
                        break
                
                if not bank_found or (account_type != 'Savings' and account_type != 'Current'):
                    print('\nYour informations are not correct.')
                    print('Try Again !\n')
                    continue

                print('\n---Thanks for completing the form---\n')
                print('\n---Welcome to the user portal---')

            else:
                account_matched = False
                while not account_matched:
                    print('\n# Please enter your information for logging in #')

                    email  = input('Email: ')
                    password = input('Password: ')
                    account_type = input('Account Type (type Savings or Current): ')
                    bank_name = input('Bank (type Bank name from the available Banks in the list ex: Brac Bank): ')

                    for bank in bank_list:
                        if(bank.name == bank_name):
                            for user in bank.user_accounts:
                                __, get_email, get_password, get_account_type, get_bank_name = user.get_info

                                if get_email == email and get_password == password and get_account_type == account_type and get_bank_name == bank_name:
                                    account_matched = True
                                    current_account = user
                                    break
                            if account_matched:
                                break

                    if account_matched:
                        print('\n--Thanks for logging in---\n') 
                    else:
                        print('\nInformation not matched try again !')
                        continue
            

            login = True            
            while login:

                print('\nYou can do the following actions--')
                print('1.Deposit:\n2.Withdraw:\n3.Check Balance:\n4.Check Transaction History:\n5.Take Loan:\n6.Transfer Amount to another account:\n7.Logout:')

                option = int(input('Enter your choice: '))

                print('')
                if option == 1:
                    amount = int(input('Enter amount: '))
                    current_account.deposit(amount)
                elif option == 2:
                    amount = int(input('Enter amount: '))
                    current_account.withdraw(amount)
                elif option == 3:
                    print(f'Your balance is {current_account.balance}')
                elif option == 4:
                    print(f'Your transaction history: {current_account.transaction_history}')
                elif option == 5:
                    amount = int(input('Enter amount: '))
                    current_account.take_loan(amount)
                elif option == 6:
                    print('--Enter the following information for your other account--')

                    email  = input('Email: ')
                    password = input('Password: ')
                    account_type = input('Account Type (type Savings or Current): ')
                    bank_name = input('Bank (type Bank name from the available Banks in the list ex: Brac Bank): ')

                    account_matched = False
                    other_account = None
                    for bank in bank_list:
                        if(bank.name == bank_name):
                            for user in bank.user_accounts:
                                __, get_email, get_password, get_account_type, get_bank_name = user.get_info

                                if get_email == email and get_password == password and  get_account_type == account_type and get_bank_name == bank_name:
                                    account_matched = True
                                    other_account = user
                                    break
                            if account_matched:
                                break

                    if account_matched:
                        current_account.transfer_amount(other_account)
                        print('Transfer was completed successfully')
                    else:
                        print('Information not matched !')
                        print('Transfer could not be completed !')
                        continue

                else:
                    print('--Thanks for using the portal--')
                    print('We hope to see you again!\n')
                    login = False
                    

            
        else:
            current_account = None

            print('\n---Welcome to the admin portal-----')
            print('1.Create new account\n2.Login')

            option = int(input('Enter your choice: '))
               

            if option == 1:
                print('\n# Please enter the following information for creating an account #')

                name = input('Name: ')
                email = input('Email: ')
                password = input('Password: ')
                address = input('Address: ')
                bank_name = input('Bank (type Bank name from the available Banks in the list ex: Brac Bank): ')


                bank_found = False
                for bank in bank_list:
                    if(bank.name == bank_name):
                        admin = Admin(name, email, address, password, bank)
                        current_account = admin
                        bank_found = True
                        break
                
                if not bank_found:
                    print('\nYour informations are not correct.')
                    print('Try Again !\n')
                    continue
                    
                print('\n---Thanks for completing the form---\n')
                print('\n---Welcome to the admin portal---\n')

            else:
                account_matched = False
                while not account_matched:
                    print('\n# Please enter your information for logging in #')

                    name = input('Name: ')
                    email  = input('Email: ')
                    password = input('Password: ')
                    bank_name = input('Bank (type Bank name from the available Banks in the list ex: Brac Bank): ')

                    for bank in bank_list:
                        if(bank.name == bank_name):
                            for admin in bank.admin_accounts:
                                get_name, get_email, get_password, __ = admin.get_info

                                if get_name == name and get_email == email and get_password == password:
                                    account_matched = True
                                    current_account = admin
                                    break
                            if account_matched:
                                break

                    if account_matched:
                        print('--Thanks for logging in---') 
                    else:
                        print('Information not matched try again !')
                        continue
            

            login = True            
            while login:

                print('\nYou can do the following actions--')
                print('1.Delete Account:\n2.View Accounts:\n3.Check Bank Balance:\n4.Check Total Loan:\n5.Set Loan Feature:\n7.Logout:')

                option = int(input('Enter your choice: '))

                print('')
                if option == 1:
                    print('Enter user info: ')
                    
                    name = input('Name: ')
                    email  = input('Email: ')
                    account_type = input('Account Type (type Savings or Current): ')

                    user_account = None
                    account_matched = False
                    for user in admin.view_accounts():
                        get_name, get_email, __, get_account_type, __ = user.get_info
                        if get_name == name and get_email == email  and  get_account_type == account_type:
                            account_matched = True
                            user_account = user
                            break
                        if account_matched:
                            break
                    
                    if account_matched:
                        current_account.delete_account(user_account)
                        print('Account deleted successfully')

                elif option == 2:
                    print(f'Users: {current_account.view_accounts()}')

                elif option == 3:
                    print(f'Bank balance is {current_account.check_bank_balance()}')
                
                elif option == 4:
                    print(f'Loan amount is: {current_account.check_bank_loans()}')
                
                elif option == 5:
                    for user in admin.view_accounts():
                        print(f'User: {user},  Account Type: {user.account_type} and Loan: {user.loan_info}')
                    

                    num = int(input('Enter number of users to change the loan feature: '))

                    for i in range(0, num):
                        feature = int(input('Turn loan feature On or Off (1 or 0): '))
                        
                        name = input('Enter user name: ')
                        account_type = input('Account Type (type Savings or Current): ')

                        for user in admin.view_accounts():
                            if user.name == name and user.account_type == account_type:
                               if feature == 1:
                                 user.loan_feature(True)
                               else:
                                   user.loan_feature(False)
                else:
                    print('\n--Thanks for using the portal--')
                    print('We hope to see you again!\n')
                    login = False
            

if __name__ == '__main__':
    main()
