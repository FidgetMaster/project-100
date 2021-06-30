class ATM(object):
    def __init__(self, cardnumber, pinnumber):
        self.cardnumber = cardnumber
        self.pinnumber = pinnumber
    def CheckBalance(self):
        print("Your balance is currently: 50000")
    def Withdraw(self, amount):
        newamount = 50000 - amount
        print("You have withdrawn " + str(amount) + " Your remaining balance is: " + str(newamount))

def NewUser():
    cardnumber = input("Enter Card Number: ")
    pinnumber = input("Enter Pin Number: ")
    User = ATM(cardnumber, pinnumber)
    print("Choose Your Activity: ")
    print("1. Balance Enquiry 2. Withdraw")
    activity = int(input("Enter Activity Number: "))
    if(activity == 1):
        User.CheckBalance()
    elif(activity == 2):
        amount = int(input("Enter Amount To Withdraw: "))
        User.Withdraw(amount)
    else:
        print("Enter A Valid Number")
NewUser()