class Account:
    owner = "NULL"
    balance = 0
    def __init__(self, name):
        owner = name

    def deposit(self, num = 0):
        if num >= 0:
            self.balance += num
            print("Getting richer:", num)

        else:
            print("Ain't that good hacker")

    def withdraw(self, num = 0):
        if num >= 0:
            if num <= self.balance:
                self.balance -= num
                print("Withdrawal:", num)

            else:
                print("you're too poor for that")

        else:
            print("Dummy?")


Person1 = Account("Person1")
Person2 = Account("Person2")

running = True
while running:
    command, *num = input().split()

    if len(num) != 0:
        num = int(num[0])

    if command == "Withdraw":
        Person1.withdraw(num)

    elif command == "Add":
        Person1.deposit(num)

    elif command == "End":
        running = False

    else:
        print("Denied")
