class User:
    # initial function
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # create an methode
    def sayHello(self):
        print("Hello {name}".format(name=self.name))


# inheritance
class Customer(User):
    def __init__(self, name, age, credit):
        super().__init__(name, age)
        self.credit = 0

    # get credit
    def getCredit(self):
        return self.credit

    def increaseCredit(self):
        self.credit += 100


customer1 = Customer("Savas", 32, 0)
print(customer1.getCredit())
customer1.increaseCredit()
print(customer1.getCredit())
"""
# create an user
user1 = User("Savas", 32)
user1.sayHello()
"""
