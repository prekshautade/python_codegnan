## Creating table
#accounts_table = {account: password}
#users_table = {account: [amount,Name,eamil]}

accounts_table = {1234:456,
                  1235:457}
users_table = {1234:[1000,'Lion','lion@gmail.com'],
               1235:[500,'Tiger','tiger@gmail.com']}


##functions
#login function definition
def login(username:int, password:int):
    #checking the account number is exist in accounts table or not
    if username in accounts_table:
        #checking the password
        if password == accounts_table[username]:
            print("Login successful")
            return True
        else:
            print("check the credentials")
            return False
    else:
        print("user not found")
        return False

#withdraw function definition
def withdraw(account:int,withdraw_amount:int):
    # checking account in users table
    if account in users_table:
       amount = users_table[account][0]
       #checking amount is sufficient or not
       if amount >= withdraw_amount:
           users_table[account][0] -= withdraw_amount
           print(f"{withdraw_amount}withdraw successful and \
                 current balance is:{users_table[account][0]}")
       else:
           print("Insufficient amount in your account")
    else:
        print("user not found")           
    
#deposite function definition
def deposite(account:int, deposite_amount:int):
    #checking account in users table
    if account in users_table:
        #validating amount
        if deposite_amount > 0:
            users_table[account][0] += deposite_amount
            print(f"{deposite_amount}deposite successful and \
                  current balance is:{users_table[account][0]}")
        else:
            print("Check with your deposite amount")
    else:
        print("user not found")            


#transfer function definition
def transfer(sender:int,reciever:int, transfer_amount:int):
    # cehcking account in users table
    if sender in users_table:
        amount = users_table[sender][0]
        #receiver account is present in users table or not
        if reciever in users_table:
       #checking amount is sufficient or not
          if amount >= transfer_amount:
             users_table[sender][0] -= transfer_amount
             users_table[reciever][0] += transfer_amount
             print(f"{transfer_amount}Transfer successful and \
                 current balance is:{users_table[sender][0]}")
          else:
           print("Insufficient amount in your account")
        else:
           print("Reciever not found")
    else:
        print("user not found")          
        #
        

#ministatement function definition
def ministatement(account:int):
    print("ministatement page development under proccessing")

# balance enquiry function defination
def balanceEnquiry(account:int):
    if account in users_table: 
        print(f"Current balance is: {users_table[account][0]}")
    else:
        print("user not found")       

#logout function definition
def logout():
    print("log out successfully")
    exit()



#main
if __name__ == "__main__":
    print("Welcome to Codegnan Bank Application")
    username = int(input("Enter your account number: "))
    password = int(input("Enter your password: "))
    login_val = login(username = username,password = password)
    while login_val:
        operations = ("1. Withdraw \n",
                      "2. Deposite \n",
                      "3. Transfer \n",
                      "4. Ministatement \n",
                      "5. balanceEnquiry \n"
                      "6. logout \n"
                      )
        print(*operations)

        choice = int(input("Select your operation:"))

        if choice == 1:
            amount = int(input("Enter your withdraw amount:"))
            withdraw(account= username, withdraw_amount= amount)

        elif choice == 2:
            amount = int(input("Enter your deposite amount:"))
            deposite(account= username, deposite_amount=amount)

        elif choice == 3:
            account = int(input("Enter reciever account number:"))
            amount = int(input("Enter your transfer amount:"))
            transfer(sender=username, reciever=account, transfer_amount=amount)

        elif choice == 4:
            ministatement(account=username)

        elif choice == 5:
            balanceEnquiry(account=username)

        elif choice == 6:
            logout()    
        else:
            print("Select your operation between 1 - 6")