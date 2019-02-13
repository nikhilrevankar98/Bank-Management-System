
#import sys;


class BankAccount:
    def __init__(self, accountNumber, name ):
        self.__accountNumber = accountNumber
        self.__name = name

    def get_account_number(self):
        return self.__accountNumber


    def get_name(self):
        return self.__name


    def set_account_number(self, value):
        self.__accountNumber = value


    def set_name(self, value):
        self.__name = value

class FixedDeposit(BankAccount):
    def __init__(self, accountNumber, name, duration, amount, rateOfInterest ):
        super().__init__(accountNumber,name)
        self.__duration = duration
        self.__amount = amount
        self.__rateOfInterest = rateOfInterest

    def get_duration(self):
        return self.__duration


    def get_amount(self):
        return self.__amount


    def get_rate_of_interest(self):
        return self.__rateOfInterest


    def set_duration(self, value):
        self.__duration = value


    def set_amount(self, value):
        self.__amount = value


    def set_rate_of_interest(self, value):
        self.__rateOfInterest = value
    
        
class RecurringDeposit(BankAccount):
    def __init__(self, accountNumber, name, duration, monthlyPayment, rateOfInterest ):
        super().__init__(accountNumber,name)
        self.__duration = duration
        self.__monthlyPayment = monthlyPayment
        self.__rateOfInterest = rateOfInterest

    def get_duration(self):
        return self.__duration


    def get_monthly_payment(self):
        return self.__monthlyPayment


    def get_rate_of_interest(self):
        return self.__rateOfInterest


    def set_duration(self, value):
        self.__duration = value


    def set_monthly_payment(self, value):
        self.__monthlyPayment = value


    def set_rate_of_interest(self, value):
        self.__rateOfInterest = value

class BankDemo:
    n=0
    ch='n'
    
    def bankOptions(self):
        print("******************************")
        print("  Bank Account Demonstration  ")
        print("******************************")
        print("1. Read & Write Fixed Deposit")
        print("2. Read & Write Recurring Deposit")
        print("3. Exit")
        
        n=int(input("\nSelect your choice : "))
        if n==1:
            self.readWriteFixedDeposit()
        elif n==2:
            self.readWriteRecurringDeposit()
        elif n==3:
            print("Thank You!!!")
            exit()
        else:
            print("invalid option!\n try again\n")
            self.bankOptions() 
    
    def readWriteFixedDeposit(self):        
        print("\nGive Fixed Deposit Details\n")
        j=0
        while(j==0):
            try:
                accountNumber = int(input("Enter Account Number: ").strip())
                j=1
            except:
                print("Please try again")
        name =input("Enter Account Name: ").strip()
        j=0
        while(j==0):
            try:
                duration = int(input("Duration: ").strip())
                j=1
            except:
                print("Please try again")
        j=0
        while(j==0):
            try:
                amount = float(input("Amount: ").strip())
                j=1
            except:
                print("Please try again")
        
        j=0
        while(j==0):
            try:
                rateOfInterest = float(input("Rate of Interest: ").strip())
                j=1
            except:
                print("Please try again")
       
        
        fd = FixedDeposit(accountNumber, name, duration, amount, rateOfInterest)
        
        print("\nFixed Deposit Details are...\n")
        print("\nAccount Number: ", fd.get_account_number())
        print("Account Name: ", fd.get_name())   
        print("Duration: ", fd.get_duration())
        print("Amount: ", fd.get_amount())
        print("Rate of Interest: ", fd.get_rate_of_interest())
        
    def readWriteRecurringDeposit(self):
        print("\nGive Recurring Deposit Details\n")
        j=0
        while(j==0):
            try:
                accountNumber = int(input("Enter Account Number: ").strip())
                j=1
            except:
                print("Please try again")
        name =input("Enter Account Name: ").strip()
        j=0
        while(j==0):
            try:
                duration = int(input("Duration: ").strip())
                j=1
            except:
                print("Please try again")
        j=0
        while(j==0):
            try:
                monthlyPayment = float(input("Monthly Payment: ").strip())
                j=1
            except:
                print("Please try again")
        
        j=0
        while(j==0):
            try:
                rateOfInterest = float(input("Rate of Interest: ").strip())
                j=1
            except:
                print("Please try again")   
      
                
        rd = RecurringDeposit(accountNumber, name, duration, monthlyPayment, rateOfInterest)
        
        print("\nRecurring Deposit Details are...\n")
        print("\nAccount Number: ", rd.get_account_number())
        print("Account Name: ", rd.get_name())   
        print("Duration: ", rd.get_duration())
        print("Monthly Payment: ", rd.get_monthly_payment())
        print("Rate of Interest: ", rd.get_rate_of_interest())    
        
    def gotooptions(self):
        if self.n!=3:
            ch=input("\nDo you wish to continue(y/n)").strip()
            if(ch[0]=='y' or ch[0]=='Y'):
                BankDemo.bankOptions(self)
            else:
                print("Thank you!")
                exit()        
        
demoObject = BankDemo()
demoObject.bankOptions()
demoObject.gotooptions()
 
