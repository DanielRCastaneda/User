class User:
    def __init__(self, name, bank_statement):
        self.name = name
        self.bank_statement = bank_statement
    
    def make_deposit(self, amount):
        self.bank_statement += amount

    def make_withdrawl(self, amount):
        self.bank_statement -= amount
    
    def display_user_balance(self):
        print(f"User {self.name} has a balance of: ${self.bank_statement}")

    def transfer_money(self, amount, user):
        self.bank_statement -= amount
        user.bank_statement += amount
        self.display_user_balance()
        user.display_user_balance()


user1 = User('Daniel',2500)
user2 = User('Liz', 500)
user3 = User('Marcos',15000)

user1.make_deposit(960)
user1.make_deposit(500)
user1.make_deposit(250)
user1.make_withdrawl(300)
user1.display_user_balance()

user2.make_deposit(10)
user2.make_deposit(400)
user2.make_withdrawl(5)
user2.make_withdrawl(80)
user2.display_user_balance()

user3.make_deposit(2500)
user3.make_withdrawl(1500)
user3.make_withdrawl(5000)
user3.make_withdrawl(2500)
user3.display_user_balance()

user1.transfer_money(500,user3)

