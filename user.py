class User:
    def __init__(self, name, bank_statement):
        self.name = name
        self.bank_statement = bank_statement
    
    def make_deposit(self, amount):
        self.bank_statement += amount
        return self

    def make_withdrawl(self, amount):
        self.bank_statement -= amount
        return self
    
    def display_user_balance(self):
        print(f"User {self.name} has a balance of: ${self.bank_statement}")
        return self

    def transfer_money(self, amount, user):
        self.bank_statement -= amount
        user.bank_statement += amount
        self.display_user_balance()
        user.display_user_balance()
        return self


user1 = User('Daniel',2500)
user2 = User('Liz', 500)
user3 = User('Marcos',15000)

user1.make_deposit(960).make_deposit(500).make_deposit(250).make_withdrawl(400).display_user_balance()


user2.make_deposit(10).make_deposit(400).make_withdrawl(5).make_withdrawl(80).display_user_balance()


user3.make_deposit(2500).make_withdrawl(1500).make_withdrawl(5000).make_withdrawl(2500).display_user_balance()


user1.transfer_money(500,user3)

