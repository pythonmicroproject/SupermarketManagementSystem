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
        print(" MANAGER MENU ".center(100,'-'),end= "\n")
        user.managerMenuHeader()
        print("\t1.Inventory Management\n")
        print("\t2.Employee Management\n")
        print("\t3.Sales Management\n")
        print("\t4.Update Store Data\n")
        print("\t5.LOG OUT\n")
        print("-"*100, end="\n\n")
        choice = input("Enter choice : ")
        if choice == '1':
            while True:
                clear()
                print(" INVENTORY MANAGEMENT ".center(100,'-'),end= "\n")
                user.managerMenuHeader()
                print("\t1.View Inventory\n")
                print("\t2.Search Product\n")
                print("\t3.Best Selling Products\n")
                print("\t4.Low Quantity Products\n")
                print("\t5.Add New Product\n")
                print("\t6.Update Product\n")
                print("\t7.Delete Product\n")
                print("\t8.Go Back...\n")
                print("-"*100, end="\n\n")
                choice = input("Enter choice : ")
                if choice == '1':
                    user.viewInventory()
                elif choice == '2':
                    user.searchProduct()
                elif choice == '3':
                    user.bestSellingProducts()
                elif choice == '4':
                    user.lowQuantityProducts()
                elif choice == '5':
                    user.addProduct()
                elif choice == '6':
                    user.updateProduct()
                elif choice == '7':
                    user.deleteProduct()
                elif choice == '8':
                    break
                else:
                    input("Please enter a valid option !\n")

        elif choice == '2':
            while True:
                clear()
                print(" EMPLOYEE MANAGEMENT ".center(100,'-'),end= "\n")
                user.managerMenuHeader()
                print("\t1.Employee List\n")
                print("\t2.Delete Employee\n")
                print("\t3.Add New Employee\n")
                print("\t4.Go Back...\n")
                print("-"*100, end="\n\n")
                choice = input("Enter choice : ")
                if choice == '1':
                    user.viewEmployee()
                elif choice == '2':
                    user.deleteEmployee()
                elif choice == '3':
                    user.addEmployee()
                elif choice == '4':
                    break
                else:
                    input("Please enter a valid option !\n")

        elif choice == '3':
            while True:
                clear()
                print(" SALES MANAGEMENT ".center(100,'-'),end= "\n")
                user.managerMenuHeader()
                print("\t1.View Sales\n")
                print("\t2.Search Bill\n")
                print("\t3.Sales Breakdown\n")
                print("\t4.Go Back...\n")
                print("-"*100, end="\n\n")
                choice = input("Enter choice : ")
                if choice == '1':
                    user.viewSales()
                elif choice == '2':
                    user.searchBill()
                elif choice == '3':
                    user.salesBreakdown()
                elif choice == '4':
                    break
                else:
                    input("Please enter a valid option !\n")

        elif choice == '4':
            user.updateStoreInfo()
        elif choice == '5':
            break
        else:
            input("Please enter a valid option !\n")

def runEmployee():
    user = employee.employee()
    if not user.employeeLogin():
        return
    while True:
        clear()
        print(" EMPLOYEE MENU ".center(100,'-'),end= "\n")
        user.employeeMenuHeader()
        print("\t1.View Inventory\n")
        print("\t2.Billing\n")
        print("\t3.Account\n")
        print("\t4.LOG OUT\n")
        print("-"*100, end="\n\n")
        choice = int(input("Enter choice : "))
        if choice == 1:
            user.viewInventory()
        elif choice == 2:
            user.cart()
        elif choice == 3:
            while True:
                clear()
                print(" ACCOUNT ".center(100,'-'),end= "\n")
                user.employeeMenuHeader()
                print("\t1.My Sales\n")
                print("\t2.Change Password\n")
                print("\t3.Go Back...\n")
                print("-"*100, end="\n\n")
                choice = input("Enter choice : ")
                if choice == '1':
                    user.mySales()
                elif choice == '2':
                    user.changeEmployeePassword()
                elif choice == '3':
                    break
                else:
                    input("Please enter a valid option !\n")

        elif choice == 4:
            break
        else:
            input("Please enter a valid option !\n")

while True:
    storeInfo = manager.storeInfoInitializer("storeInfoFile.txt")
    clear()
    print("-"*100)
    print(storeInfo['name'].center(100))
    print(storeInfo['city'].center(100))
    print((storeInfo['state']+" - "+storeInfo['pincode']).center(100))
    print(("Phone: "+storeInfo['phone']).center(100))
    print(end="\n")
    print(" MENU ".center(100,"-"),end="\n\n")
    print("\t1.Employee\n")
    print("\t2.Manager\n")
    print("\t3.EXIT\n")
    print("-"*100, end="\n\n")
    choice = input("Enter choice : ")
    if choice == '1':
        runEmployee()
    elif choice == '2':
        runManager()
    elif choice == '3':
        break
    else:
        input("Please enter a valid option !\n")
