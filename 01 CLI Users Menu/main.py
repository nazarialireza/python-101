class User:
    def __int__(self):
        self.id = None
        self.username = None
        self.address = None
        self.phone = None


employees = []


def render():
    if temp == 9:
        init()
        return int(input('>>> '))
    elif temp == 1:
        return add()
    else:
        return 0


def add():
    print(2 * "\n")
    print("\t Please inset user info: ")
    user = User()
    user.id = input('\tID: ')
    user.username = input('\tUsername: ')
    user.address = input('\tAddress: ')
    user.phone = input('\tPhone: ')
    employees.append(user)
    print("\t" + 20 * "*")
    print(2 * "\n")
    return int(input("(1) Add | (9) Back | (0) Exit \n" + ">>> "))


def edit():
    find = False
    print(2 * "\n")
    user_id = int(input("\t Please enter user id: "))
    for i, u in enumerate(employees):
        if user_id == int(u.id):
            user = User()
            user.id = input('\tID: ')
            user.username = input('\tUsername: ')
            user.address = input('\tAddress: ')
            user.phone = input('\tPhone: ')
            employees.pop(i)
            employees.append(user)
            find = True
            print("User " + str(user_id) + " have been updated")

    if not find:
        print("User " + str(user_id) + " are not in the list")
    print(2 * "\n")
    return int(input("(9) Back | (0) Exit \n" + ">>> "))


def display():
    print(2 * "\n")
    if len(employees) > 0:
        for i, u in enumerate(employees):
            print("\tRow ID: " + str(i + 1) + " " + str(20 * "*"))
            print("\tUser: (" + u.id + ") " + u.username + ", " + u.address + ", " + u.phone)
            print("\t" + 30 * "-")
    else:
        print("There no registered user ")
    print(2 * "\n")
    return int(input("(9) Back | (0) Exit \n" + ">>> "))


def delete():
    print(2 * "\n")
    user_id = int(input("Enter row id to remove the user: "))
    if user_id <= len(employees):
        employees.pop(user_id - 1)
        print("User " + str(user_id) + " have been removed")
    else:
        print("User " + str(user_id) + " is out of list")
    print(2 * "\n")
    return int(input("(9) Back | (0) Exit \n" + ">>> "))


def init():
    print(2 * "\n")
    print("Employee listing application")
    print("Select option for operation")
    print("\t(1) Add new")
    print("\t(2) Edit form list")
    print("\t(3) Delete form list")
    print("\t(4) Browse the list")
    print("\t" + 20 * "-")
    print("\t(0) Exit")
    print(2 * "\n")


init()
mainIO = int(input('>>> '))
while mainIO != 0:
    if mainIO == 1:
        temp = add()
        mainIO = render()
    elif mainIO == 2:
        temp = edit()
        mainIO = render()
    elif mainIO == 3:
        temp = delete()
        mainIO = render()
    elif mainIO == 4:
        temp = display()
        mainIO = render()
    else:
        init()
        mainIO = int(input('>>> '))

print("Thanks!")
