class mfile:
    def __init__(self,file):
        self.fname=file
    def fcwrite(self,data):
        try:
            f=open(self.fname,"a")
            f.write(data)
            f.close()
            print("content written successfully")
        except:
            print("File doesn't exist")
    def fcread(self):
        try:
            f=open(self.fname,"r")
            for line in f:
                print(line.strip())
            f.close()
        except:
            print("File doesn't exists")

class atm(mfile):
    def __init__(self,file):
        super().__init__(file)
        self.balance=0
        self.pin=0
    def runatm(self):
        print("*********** Welcome to my ATM ***********")
        while True:
            self.balance=int(input("Enter initial balance:"))
            if self.balance>0:break
            print("Invalid balance")
        while True:
            self.pin=int(input("Enter 4 digit pin:"))
            if 1000<=self.pin<=9999:break
            print("Invalid pin")
        while True:
            print("\n1.Check Balance\n2.Withdraw\n3.Deposit\n4.Change PIN\n5.Show Transactions\n6.Exit")
            num=int(input("Enter choice:"))
            if num==1:
                attempt=0
                while attempt<3:
                    upin=int(input("Enter pin:"))
                    if upin==self.pin:
                        print("Balance:",self.balance)
                        self.fcwrite(f"Balance:{self.balance}\n\n")
                        break
                    else:
                        attempt+=1
                        print("Wrong pin",3-attempt,"attempts left")
            elif num==2:
                attempt=0
                while attempt<3:
                    upin=int(input("Enter pin:"))
                    if upin==self.pin:
                        while True:
                            w=int(input("Enter withdraw amount:"))
                            if 0<w<=self.balance:
                                self.balance-=w
                                print("Withdrawn:",w)
                                print("Balance:",self.balance)
                                self.fcwrite(f"Withdraw:{w}\nBalance:{self.balance}\n\n")
                                break
                            else:
                                print("Invalid amount")
                        break
                    else:
                        attempt+=1
                        print("Wrong pin",3-attempt,"attempts left")
            elif num==3:
                attempt=0
                while attempt<3:
                    upin=int(input("Enter pin:"))
                    if upin==self.pin:
                        d=int(input("Enter deposit amount:"))
                        if d>0:
                            self.balance+=d
                            print("Deposited:",d)
                            print("Balance:",self.balance)
                            self.fcwrite(f"Deposit:{d}\nBalance:{self.balance}\n\n")
                        else:
                            print("Invalid amount")
                        break
                    else:
                        attempt+=1
                        print("Wrong pin",3-attempt,"attempts left")
            elif num==4:
                attempt=0
                while attempt<3:
                    upin=int(input("Enter pin:"))
                    if upin==self.pin:
                        while True:
                            np=int(input("Enter new pin:"))
                            if 1000<=np<=9999:
                                self.pin=np
                                print("Pin changed")
                                break
                            else:
                                print("Invalid pin")
                        break
                    else:
                        attempt+=1
                        print("Wrong pin",3-attempt,"attempts left")
            elif num==5:
                print("Transactions:")
                self.fcread()
            elif num==6:
                print("Thank you")
                break
            else:
                print("Invalid choice")

bank=atm("info.txt")
bank.runatm()