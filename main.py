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
    if not user.managerLogin():
        return
    while True:
        clear()
        print("-" * 30, "MANAGER MENU", "-" * 33, "\n")
        print("\t1.Inventory Management\n")
        print("\t2.Employee Management\n")
        print("\t3.Sales Management\n")
        print("\t4.LOG OUT\n")
        choice = input("Enter choice : ")
        if choice == '1':
            while True:
                clear()
                print("-" * 30, "Inventory Management", "-" * 33, "\n")
                print("\t1.View Inventory\n")
                print("\t2.Add New Product\n")
                print("\t3.Update Product\n")
                print("\t4.Delete Product\n")
                print("\t5.Go Back...\n")
                choice = input("Enter choice : ")
                if choice == '1':
                    user.viewInventory()
                elif choice == '2':
                    user.addProduct()
                elif choice == '3':
                    user.updateProduct()
                elif choice == '4':
                    user.deleteProduct()
                elif choice == '5':
                    break
                else:
                    input("Please enter a valid option !\n")

        elif choice == '2':
            while True:
                clear()
                print("-" * 30, "Employee Management", "-" * 33, "\n")
                print("\t1.Add New Employee\n")
                print("\t2.Delete Employee\n")
                print("\t3.Employee List\n")
                print("\t4.Go Back...\n")
                choice = input("Enter choice : ")
                if choice == '1':
                    user.addEmployee()
                elif choice == '2':
                    user.deleteEmployee()
                elif choice == '3':
                    user.viewEmployee()
                elif choice == '4':
                    break
                else:
                    input("Please enter a valid option !\n")

        elif choice == '3':
            while True:
                clear()
                print("-" * 30, "Sales Management", "-" * 33, "\n")
                print("\t1.View Sales\n")
                print("\t2.Go Back...\n")
                choice = input("Enter choice : ")
                if choice == '1':
                    user.viewSales()
                elif choice == '2':
                    break
                else:
                    input("Please enter a valid option !\n")


        elif choice == '4':
            break
        else:
            input("Please enter a valid option !\n")

def runEmployee():
    user = employee.employee()
    if not user.employeeLogin():
        return
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
            input("Please enter a valid option !\n")

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
        input("Please enter a valid option !\n")
