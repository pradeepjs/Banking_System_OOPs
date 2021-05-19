class User:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal Details")
        print("Name ",self.name)
        print("Age ", self.age)
        print("Gender ",self.gender)


class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance=0

    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance+self.amount
        print("Your deposit: ",self.balance)

    def withdraw(self,amount):
        self.amount = amount

        if amount>self.balance:
            print("Insuficient Fund ! availabe balance is: ",self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance has been updated:",self.balance)
    def view_Available_Balance(self):
        self.show_details()
        print("Account balance is ",self.balance)

Pramod = Bank("Pramod",25,"Male")
Pramod.deposit(5000)
Pramod.withdraw(2000)
Pramod.withdraw(5000)
print(" ")
Pramod.view_Available_Balance()