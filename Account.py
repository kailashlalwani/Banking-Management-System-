import pickle    
import os
import pathlib
class Account:
    accNo = 0           
    accName = ''        # Name of Account in String value
    accType = ''        # Type of account i.e Saving or Current
    deposit = 0         # initial deposite money = 0
    
    def CreateAccount(self):
        self.accNo = int(input("Enter the Account Number :"))
        self.accName = input("Enter the Accont-Holder Name :")
        self.accType = input("Enter the Type of Account that you want to Open(Savings or Current) :")
        self.deposit = int(input("Enter the Initial deposite Amount (>=3000 for Savings and >=10000 for Current :"))
        print("Account Created Successfully")


    def ShowAccount(self):
        print("Account Number is :", self.accNo)
        print("Account Name is :", self.accName)
        print("Type of Account is :", self.accType)
        print("Account Balance is :", self.deposit)


    def ModifyAccountDetails(self):
        print("Account Number is :" ,self.accNo)
        self.accName = input("Modify Account name is :")
        self.accType =input("Modify Account type is :")
        self.deposit = int(input("Modify Account Balance is :"))

    def DepositAmount(self, amount):
        self.deposit += amount           # Amount Increase when Deposit

    def WithdrawAmount(self, amount):
        self.deposit -= amount           # Amount Decrease when Withdraw

    def report(self):
        print(self.accNo, " ", self.accName, " ", self.accType, " ", self.deposit)

    def getAccountNumber(self):
        return self.accNo
    
    def getAccountHoldername(self):
        return self.accName

    def getAccountType(self):
        return self.accType

    def getDepositAmount(self):
        return self.deposit

def intro():
    print("\t\t\t\t**********************")
    print("\t\t\t\tBANK MANAGEMENT SYSTEM")
    print("\t\t\t\t**********************")
    
    

def writeAccount():
    account = Account()
    account.CreateAccount()
    writeAccountsFile(account)


def displayAll():
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        for item in mylist:
            print(item.accNo, " ", item.accName, " ", item.accType, " ", item.deposit)
        infile.close()        # for close a open file in python
    else:
        print("No Recors to Display")




def displaySp(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist:
            if item.accNo == num :
                print("Your Account Balance is :",item.deposit)
                found = True
    else:
        print("No records to Search")
    if not found :
        print("No Existing record found with this Number")


def depositAndWithdraw(num1 , num2):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data' , 'rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist:
            if item.accNo == num1:
                if num2 == 1:
                    amount = int(input("Enter the Amoun to be Deposite"))
                    item.deposit += amount
                    print("Your Account is Updated")
                elif num2 == 2:
                    amount = int(input("Enter the Amount to be Withdrawn"))
                    if amount <= item.deposit:
                        item.deposit -= amount
                    else:
                        print("Insufficent Balance")
    else:
        print("No Records to Search")
    outfile = open('newaccounts.data' ,'wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')


def deleteAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data' , 'rb')
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []
        for item in oldlist:
            if item.accNo != num:
                newlist.append(item)
            os.remove('accounts.data')
            outfile = open('newaccounts.data', 'wb')
            pickle.dump(newlist,outfile)
            outfile.close()
            os.rename('newaccounts.data', 'accounts.data')

def ModifyAccountDetails(num):
    file = pathlib.path("accounts.data")
    if file.exists():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in oldlist:
            if item.accNo == num:
                item.name = input("Enter the Account Holder Name :") 
                item.type = input("Enter the Type of Account")
                item.deposit = int(input("Enter the Amount :"))

        outfile = open('newaccounts.data', 'wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data' , 'accounts.data')

def writeAccountsFile(account):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data', 'rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove("accounts.data")
    else:
        oldlist = [account]
    outfile = open('newaccounts.data','wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newaccounts.data' ,'accounts.data')


# Lets start the programme
ch = ''
num = 0
intro()

while ch != 8:
	#system("cls");
    print("\tMain Menu")
    print("\t1. New Account")
    print("\t2. Deposit Amount")
    print("\t3. Withdram Amount")
    print("\t4. Balanced Enquiry")
    print("\t5. All Account Holder List")
    print("\t6. Close an Account")
    print("\t7. Mofify An Account")
    print("\t8. Exit")
    print("Select Your Option That You Want to Process from (1-8) :")
    ch = input()
    #system("cls");

    if ch =='1':
        writeAccount()
    elif ch == '2':
        num = int(input("\tEnter the Account Number :"))
        depositAndWithdraw(num, 1)
    elif ch == '3':
        num = int(input("\tEnter the Account Number :"))
        depositAndWithdraw(num, 2)
    elif ch == "4":
        num = int(input("\tEnter the Account Number :"))
        displaySp(num)
    elif ch == '5':
        displayAll()
    elif ch=='6':
        num = int(input("\tEnter the Account Number :"))
        deleteAccount(num)
    elif ch == '7':
        num = int(input("\tEnter the Account Number :"))
        ModifyAccountDetails(num)
    elif ch == '8':
        print("\tThanks for Using Bank Management System")
        break
    else:
        print("Invailid choice")

    ch = input("Enter your Choice :")