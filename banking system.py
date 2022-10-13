
print("WELCOME TO OUR BANKING APPLICATION")
options=int(input("""Press 1----- To create account
Press 2----- To Transact \n"""))


email=""
password=""
def createAccount(email,password):
    email+=input("please enter your email\n ")
    password+=input("please enter your password\n ")
    return password

transaction=True
def deposit(amount,BAL):
     return BAL+amount   
def withdraw(amount,BAL):
    if amount > BAL:
       return deposit(amount,BAL)
    else:
        return BAL-amount    
def transfer(amount,BAL):
    return BAL-+amount    
def checkBalance(BAL):
    return f"current balance: {BAL}"


balance=0
if options==1:
    createAccount(email,password)
    balance=0
    print("Thanks for creating account with us")
    print(f"Your present balance is {balance}")   
else:
    authenticator=createAccount(password,email)
    password=input("please input your password\n ")
    if password==authenticator:
        transaction=True       
        another_transaction="yes"
        while (another_transaction=="yes"):
    
            actions=int(input(("""
            press 1----- Check balance
            press 2----- Deposit
            press 3----- Withdraw
            press 4----- Transfer\n""")))
            if actions==1:
                print(f"Your current balanceis : {checkBalance(BAL)}")
            elif actions==2:
                BAL=int(input("Enter your baalance: "))
                amount=int(input("Enter the amount: " ))
                print(f"The amount deposit is {amount}")
                print(f"Your balance is: {deposit(amount,BAL)}")
               
            elif actions==3:
                BAL=int(input("Enter your baalance: "))
                amount=int(input("enter the amount: "))
                print(f"The amount withdrawn is {amount}")
                print(f"Your balance is: {withdraw(amount,BAL)}")
                
            elif actions==4:  
                BALi=int(input("Enter your baalance: "))
                amount=int(input("Enter the amount: "))
                print(f"The amount transferred is {amount}")
                print(f"Your balance is{transfer(amount,BAL)}")
            else:
                print("Select any of the option above")
            print("Would you like to perform another transaction?.......Press yes")
            another_transaction=input()             
    else:
        
        transaction=False
        print("You do not have account an account with us!!! Proceed to create account? ")
        createAccount(email,password)





         

    
    
    




    