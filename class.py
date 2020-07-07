class User:
    # initial function
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # create an methode
    def sayHello(self):
        print("Hello {name}".format(name=self.name))


# create an user
user1 = User("Savas", 32)
user1.sayHello()
