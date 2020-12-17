import manager
import employee
import os

def clear():
    # for windows
    if os.name == 'nt':
        os.system('cls')
    # for mac and linux(os.name is 'posix')
    else:
        os.system('clear')

def runManager():
    user = manager.manager()
    while True:
        clear()
        print("-" * 30, "MANAGER MENU", "-" * 33, "\n")
        print("\t1.View Inventory\n")
        print("\t2.Add New Product\n")
        print("\t3.Update Product\n")
        print("\t4.Delete Product\n")
        print("\t5.LOG OUT\n")
        choice = int(input("Enter choice : "))
        if choice == 1:
            user.viewInventory()
        elif choice == 2:
            user.addProduct()
        elif choice == 3:
            user.updateProduct()
            pass
        elif choice == 4:
            user.deleteProduct()
            pass
        elif choice == 5:
            break
        else:
            print("Please enter a valid option !\n")
        input("Press Enter to continue...")

def runEmployee():
    user = employee.employee()
    while True:
        clear()
        print("-" * 30, "EMPLOYEE MENU", "-" * 33, "\n")
        print("\t1.View Inventory\n")
        print("\t2.Billing\n")
        print("\t3.Update Account\n")
        print("\t4.LOG OUT\n")
        choice = int(input("Enter choice : "))
        if choice == 1:
            user.viewInventory()
        elif choice == 2:
            user.cart()
        elif choice == 3:
            pass
        elif choice == 4:
            break
        else:
            print("Please enter a valid option !\n")
        input("Press Enter to continue...")

while True:
    clear()
    print("-" * 30, "MENU", "-" * 33, "\n")
    print("\t1.Employee\n")
    print("\t2.Manager\n")
    print("\t3.EXIT\n")
    choice = int(input("Enter choice : "))
    if choice == 1:
        runEmployee()
    elif choice == 2:
        runManager()
    elif choice == 3:
        break
    else:
        print("Please enter a valid option !\n")
